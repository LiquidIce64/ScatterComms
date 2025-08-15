from PySide6.QtWidgets import QWidget


from .ui_menu_widget import Ui_menu_widget
from .menu_button import MenuButton


class MenuWidget(QWidget, Ui_menu_widget):
    def __init__(self, main_page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.main_page = main_page

        self.setupButtons()
        self.attach()

        self.setFocus()

    def add_button(self, label=None, icon=None, margin=0):
        btn = MenuButton(label, icon, invert_layout=True)
        if margin > 0:
            btn.icon.setStyleSheet(f'margin:{margin}px;')
        self.layout_menu.addWidget(btn)
        return btn

    def setupButtons(self): pass

    def attach(self): pass
