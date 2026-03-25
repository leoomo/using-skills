#!/usr/bin/env python3
"""Scan local network for iReader device on port 10123."""

import socket
import subprocess
import sys
import ipaddress
import concurrent.futures


def check_port(ip, port=10123, timeout=2):
    """Check if a port is open on the given IP."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((str(ip), port))
        sock.close()
        return result == 0
    except Exception:
        return False


def get_local_network():
    """Get the local network range from current IP."""
    try:
        # Get default gateway interface
        result = subprocess.run(
            ["ipconfig", "getifaddr", "en0"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            ip = result.stdout.strip()
            # Extract 192.168.x.0/24 from the IP
            parts = ip.split('.')
            if parts[0] == '192' and parts[1] == '168':
                return f"192.168.{parts[2]}.0/24"
    except Exception:
        pass

    # Fallback: scan common 192.168.x.x ranges
    return None


def scan_network(network_cidr=None, port=10123):
    """Scan network for open port."""
    found_ips = []

    if network_cidr:
        # Scan specific network
        networks = [network_cidr]
    else:
        # Scan common 192.168.x.0/24 ranges
        networks = [f"192.168.{i}.0/24" for i in range(256)]

    for network in networks:
        try:
            net = ipaddress.ip_network(network, strict=False)
            all_hosts = list(net.hosts())

            # Prioritize common device IP ranges first (1-50, then 100-150, then rest)
            priority_hosts = all_hosts[:50] + all_hosts[100:150] + all_hosts[50:100] + all_hosts[150:]

            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                future_to_ip = {executor.submit(check_port, ip, port): ip for ip in priority_hosts}
                for future in concurrent.futures.as_completed(future_to_ip):
                    ip = future_to_ip[future]
                    try:
                        if future.result():
                            found_ips.append(str(ip))
                            print(f"Found iReader at: {ip}", file=sys.stderr)
                            return found_ips  # Return first match
                    except Exception:
                        pass
        except Exception as e:
            print(f"Error scanning {network}: {e}", file=sys.stderr)

    return found_ips


def main():
    """Main entry point."""
    # Try to get specific network first
    network = get_local_network()

    if network:
        print(f"Scanning network: {network}", file=sys.stderr)
        found = scan_network(network)
    else:
        print("Scanning common 192.168.x.x ranges...", file=sys.stderr)
        found = scan_network()

    if found:
        print(found[0])  # Print first found IP to stdout
        return 0
    else:
        print("No iReader found on port 10123", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
