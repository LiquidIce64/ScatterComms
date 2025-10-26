from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QCursor, QIcon

from widgets.common import IconWidget


class MenuButton(QFrame):
    def __init__(
        self, text: str, icon: QIcon = None,
        icon_margin=0, icon_on_left=True, override_icon_color=True
    ):
        super().__init__()
        self.setObjectName('menu_btn')
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setStyleSheet('''
            MenuButton {border-radius: 6px;}
            MenuButton:hover, MenuButton:focus {background-color: #454545;}
            #btn_label {font-size: 11pt; font-weight: 600;}
            
            MenuButton[danger="true"]:hover, MenuButton[danger="true"]:focus {background-color: #563434;}
            MenuButton[danger="true"] #btn_label {color: #FF8080;}
            MenuButton[danger="true"] #btn_icon {color: #FF8080;}
        ''')

        self.layout_btn = QHBoxLayout(self)
        self.layout_btn.setObjectName('layout_btn')
        self.layout_btn.setContentsMargins(6, 6, 6, 6)
        self.layout_btn.setSpacing(6)

        self.label = QLabel(QCoreApplication.translate('menu_btn', text), parent=self)
        self.label.setObjectName('btn_label')

        self.icon = IconWidget(self)
        self.icon.setObjectName('btn_icon')
        self.icon.setFixedSize(24, 24)
        self.icon.setContentsMargins(
            icon_margin, icon_margin, icon_margin, icon_margin
        )
        if icon is not None:
            self.icon.setIcon(icon, override_icon_color)

        if icon_on_left:
            self.layout_btn.addWidget(self.icon)
            self.layout_btn.addWidget(self.label)
        else:
            self.layout_btn.addWidget(self.label)
            self.layout_btn.addWidget(self.icon)
