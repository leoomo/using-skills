"""Image handler for downloading and processing images."""
import re
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from pathlib import Path
from typing import List, Dict, Tuple
from PIL import Image
from io import BytesIO


def extract_image_urls(content: str) -> List[str]:
    """Extract all image URLs from markdown content."""
    pattern = r'!\[([^\]]*)\]\(([^\)]+)\)'
    matches = re.findall(pattern, content)
    return [url for _, url in matches]


def is_external_url(url: str) -> bool:
    """Check if URL is external (http/https)."""
    return url.startswith('http://') or url.startswith('https://')


def download_image(url: str, timeout: int = 8) -> bytes:
    """Download image from URL, return bytes or None on failure."""
    try:
        response = requests.get(url, timeout=timeout, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"  Warning: Failed to download image {url}: {e}")
        return None


def optimize_image(image_data: bytes, max_size: int = 1200, quality: int = 85) -> bytes:
    """Resize and compress image for e-readers."""
    try:
        img = Image.open(BytesIO(image_data))

        # Convert to RGB if necessary
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')

        # Resize if too large
        width, height = img.size
        if max(width, height) > max_size:
            ratio = max_size / max(width, height)
            new_size = (int(width * ratio), int(height * ratio))
            img = img.resize(new_size, Image.LANCZOS)

        # Save as JPEG
        output = BytesIO()
        img.save(output, format='JPEG', quality=quality, optimize=True)
        return output.getvalue()
    except Exception as e:
        print(f"  Warning: Failed to optimize image: {e}")
        return image_data


def _download_and_process(url: str) -> Tuple[str, str, bytes]:
    """Download and process a single image. Returns (url, filename, data)."""
    url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
    image_data = download_image(url)
    if image_data:
        optimized = optimize_image(image_data)
        filename = f"img_{url_hash}.jpg"
        return url, filename, optimized
    return url, None, None


def process_images(content: str, base_path: Path, image_map: Dict[str, str] = None) -> Tuple[str, Dict[str, bytes]]:
    """
    Process all images in content with concurrent downloads.
    Returns: (updated_content, image_data_dict)
    """
    if image_map is None:
        image_map = {}

    urls = extract_image_urls(content)
    images_data = {}

    # Separate external vs local images
    external_urls = []
    local_urls = []
    for url in urls:
        if url in image_map:
            continue
        if is_external_url(url):
            external_urls.append(url)
        else:
            local_urls.append(url)

    # Download external images concurrently
    if external_urls:
        print(f"  Downloading {len(external_urls)} images...")
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(_download_and_process, url): url for url in external_urls}
            for future in as_completed(futures):
                url, filename, data = future.result()
                if filename:
                    images_data[filename] = data
                    image_map[url] = f"images/{filename}"

    # Handle local images
    for url in local_urls:
        local_path = base_path / url.lstrip('./')
        if local_path.exists():
            with open(local_path, 'rb') as f:
                image_data = f.read()
            optimized = optimize_image(image_data)
            url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
            ext = local_path.suffix.lstrip('.') or 'jpg'
            filename = f"img_{url_hash}.{ext}"
            images_data[filename] = optimized
            image_map[url] = f"images/{filename}"

    # Update content with new paths
    for original_url, new_path in image_map.items():
        content = content.replace(f"]({original_url})", f"]({new_path})")

    return content, images_data
