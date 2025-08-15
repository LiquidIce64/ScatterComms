from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QPixmap, QIcon

from .ui_menu_button import Ui_menu_button


class MenuButton(QWidget, Ui_menu_button):
    def __init__(self, label: str = None, icon: QPixmap | QIcon = None, *args, invert_layout=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.clicked = self.btn.clicked

        if label is not None:
            self.label.setText(label)
        if icon is not None:
            if isinstance(icon, QPixmap):
                icon = QIcon(icon)
            self.icon.setIcon(icon)
        if invert_layout:
            self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
