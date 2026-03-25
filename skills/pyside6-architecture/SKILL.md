---
name: pyside6-architecture
description: 使用 PySide6 构建高性能桌面应用，遵循 MVC/MVVM 架构模式。涵盖多线程、信号槽、类型提示、资源管理等最佳实践。
version: 1.0.0
---

# PySide6 架构开发技能

当你被要求使用 PySide6 开发 Python 桌面应用程序时，请严格遵守以下规则。

## 1. 核心架构准则：强制 MVC/MVVM

所有生成的方案必须严格遵守 Model-View-Controller (MVC) 或 MVVM 模式：

### Model (模型层)
- 仅负责原始数据、业务逻辑、数据库交互或 API 请求
- **严禁导入** `PySide6.QtWidgets` 或任何 UI 相关模块
- 通过信号发出数据变化通知

### View (视图层)
- 仅负责 UI 布局、样式 (QSS) 和控件声明
- 通过 `Signal` 发出用户交互信号
- 绝不包含业务逻辑

### Controller/ViewModel (逻辑层)
- 作为中介，订阅 View 的信号
- 调用 Model 进行处理
- 通过信号将结果回馈给 View

## 2. 编码与技术规范

### Threading (多线程)
任何耗时操作必须封装在 `QThread` 或 `QRunnable` 中：

```python
from PySide6.QtCore import QThread, Signal

class Worker(QThread):
    finished = Signal(dict)
    progress = Signal(int)
    error = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = None

    def run(self) -> None:
        try:
            result = self._process_data()
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))

    def _process_data(self) -> dict:
        # 耗时操作
        pass
```

### OOP (面向对象)
必须使用基于类 (Class-based) 的开发：

```python
# ❌ 禁止：全局作用域业务逻辑
def process_data():
    ...

# ✅ 正确：类方法
class DataProcessor:
    def process(self, data: str) -> dict:
        ...
```

### Type Hints (类型提示)
所有函数参数和返回值必须包含完整的类型注解：

```python
# ❌ 错误
def process(data):
    return data

# ✅ 正确
def process(self, data: str) -> dict[str, Any]:
    return {"result": data}
```

### Signal & Slot (信号槽)
优先使用 PySide6 新式信号语法：

```python
from PySide6.QtCore import Signal, Slot

class MyWidget(QWidget):
    # 新式信号语法
    data_ready = Signal(dict)
    error_occurred = Signal(str)

    @Slot()
    def on_button_clicked(self) -> None:
        ...

    @Slot(str)
    def on_input_changed(self, text: str) -> None:
        ...
```

### Resource Management (资源管理)
正确处理对象的 `parent` 关系：

```python
# ✅ 正确：使用 parent 参数
button = QPushButton("Click", parent=self)

# ✅ 正确：使用 with 语句
with open("file.txt", "r") as f:
    content = f.read()
```

## 3. UI 与用户体验

### Responsive Layout
严禁使用绝对定位，必须使用布局管理器：

```python
# ❌ 禁止：绝对定位
button.setGeometry(100, 100, 80, 30)

# ✅ 正确：布局管理器
layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(label)
self.setLayout(layout)
```

### High DPI 支持
必须包含高分屏缩放初始化：

```python
from PySide6.QtCore import Qt

if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    app = QApplication()
    window = MainWindow()
    window.show()
```

### QSS Styling
将 QSS 样式与逻辑分离：

```python
# styles/main.qss
QPushButton {
    background-color: #007acc;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
}

QPushButton:hover {
    background-color: #005a9e;
}
```

```python
# 加载 QSS
def load_stylesheet(app: QApplication) -> None:
    with open("styles/main.qss", "r") as f:
        app.setStyleSheet(f.read())
```

## 4. 项目结构

```
my_app/
├── __main__.py               # 入口点
├── app.py                    # 应用初始化
├── model/
│   ├── __init__.py
│   ├── base.py              # BaseModel
│   └── user.py              # 领域模型
├── view/
│   ├── __init__.py
│   ├── base.py              # BaseView
│   ├── main_window.py       # 主窗口
│   └── widgets/             # 自定义控件
├── controller/
│   ├── __init__.py
│   ├── base.py              # BaseController
│   └── main_controller.py   # 主控制器
├── service/
│   ├── __init__.py
│   └── api.py               # API 服务
├── styles/
│   ├── main.qss
│   └── dark.qss
└── resources/
    └── icons/
```

## 5. 基础类模板

### BaseModel

```python
from PySide6.QtCore import QObject, Signal
from datetime import datetime
from typing import Any

class BaseModel(QObject):
    """模型基类"""
    changed = Signal()

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._created_at = datetime.now()
        self._updated_at = datetime.now()

    def to_dict(self) -> dict[str, Any]:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "BaseModel":
        raise NotImplementedError
```

### BaseView

```python
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

class BaseView(QWidget):
    """视图基类"""
    # 视图发出的信号
    action_triggered = Signal(str)  # action_name

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._controller = None
        self._init_ui()
        self._connect_signals()

    def _init_ui(self) -> None:
        """初始化 UI - 子类实现"""
        raise NotImplementedError

    def _connect_signals(self) -> None:
        """连接信号 - 子类实现"""
        raise NotImplementedError

    def set_controller(self, controller: object) -> None:
        self._controller = controller

    def refresh(self) -> None:
        """刷新视图 - 子类实现"""
        pass
```

### BaseController

```python
from PySide6.QtCore import QObject, Signal

class BaseController(QObject):
    """控制器基类"""
    data_updated = Signal(object)

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._views: list[object] = []

    def register_view(self, view: BaseView) -> None:
        if view not in self._views:
            self._views.append(view)
            view.set_controller(self)

    def notify_views(self) -> None:
        for view in self._views:
            view.refresh()

    def cleanup(self) -> None:
        self._views.clear()
```

## 6. 错误处理

必须包含完善的异常捕获：

```python
from PySide6.QtWidgets import QMessageBox

def handle_error(self, error: Exception) -> None:
    """统一错误处理"""
    QMessageBox.critical(
        self,
        "错误",
        f"操作失败：{str(error)}",
        QMessageBox.Ok
    )
```

## 7. 交互协议

在提供完整代码前，请先简述该功能的**逻辑架构设计**。

---

## 使用方法

```bash
/pyside6-architecture
```

## 执行指令

当用户调用此技能时：

1. **确认需求**: 理解用户要构建的功能
2. **架构设计**: 先描述 MVC/MVVM 架构
3. **编码实现**: 遵循上述规范生成代码
4. **文件分离**: 明确告知代码所属文件
