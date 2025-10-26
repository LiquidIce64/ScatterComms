from PySide6.QtWidgets import QMenu, QWidgetAction
from PySide6.QtGui import QIcon, QMouseEvent

from .menu_button import MenuButton


class MenuWidget(QMenu):
    def __init__(self, *args, icons_on_left=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.__icons_on_left = icons_on_left
        self.setObjectName('menu_widget')
        self.setStyleSheet('''
            MenuWidget {
               border: 1px solid #404040;
               border-radius: 6px;
               background-color: #303030;
               padding: 6px;
            }
            MenuWidget::separator {
               height: 1px;
               background-color: #404040;
               margin: 3px 6px 3px 6px;
               border: none;
            }
        ''')

    def add_button(
        self, text: str, icon: QIcon = None, icon_margin=0, /,
        slot=None, danger=False, override_icon_color=True
    ):
        btn = MenuButton(
            text, icon, icon_margin,
            self.__icons_on_left, override_icon_color
        )
        btn.setParent(self)
        if danger:
            btn.setProperty('danger', True)
        action = QWidgetAction(self)
        action.setDefaultWidget(btn)
        if slot is not None:
            action.triggered.connect(slot)
        self.addAction(action)
        return btn, action

    def mousePressEvent(self, event: QMouseEvent):
        if self.geometry().contains(event.globalPos()):
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if self.geometry().contains(event.globalPos()):
            super().mouseReleaseEvent(event)
        else:
            self.hide()
