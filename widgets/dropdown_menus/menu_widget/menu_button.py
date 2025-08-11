from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QMouseEvent, QPixmap

from .ui_menu_button import Ui_menu_button


class MenuButton(QWidget, Ui_menu_button):
    clicked = Signal(QMouseEvent)

    def __init__(self, label: str = None, icon: QPixmap = None, *args, invert_layout=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        if label is not None:
            self.label.setText(label)
        if icon is not None:
            self.icon.setPixmap(icon)
        if invert_layout:
            self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.clicked.emit(event)
