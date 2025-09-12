from typing import TYPE_CHECKING
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFocusEvent

from .ui_menu_widget import Ui_menu_widget
from .menu_button import MenuButton

if TYPE_CHECKING:
    from widgets.main_page import MainPage


class MenuWidget(QWidget, Ui_menu_widget):
    focusLost = Signal(QFocusEvent)
    grid_layout_args = (1, 1, 1, 1)
    _left_side_icons = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def add_button(self, label=None, icon=None, icon_margin=2):
        btn = MenuButton(label, icon, invert_layout=self._left_side_icons)
        if icon_margin > 0:
            btn.icon.setStyleSheet(f'margin:{icon_margin}px;')
        btn.focusLost.connect(self.focusOutEvent)
        self.layout_menu.addWidget(btn)
        return btn

    def connect_button_signals(self, main_page: 'MainPage'): pass

    def focusOutEvent(self, event):
        for i in range(self.layout_menu.count()):
            widget = self.layout_menu.itemAt(i).widget()
            if widget and widget.hasFocus():
                break
        else:
            self.focusLost.emit(event)
