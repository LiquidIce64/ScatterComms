from PySide6.QtWidgets import QWidget


from .ui_menu_widget import Ui_menu_widget


class MenuWidget(QWidget, Ui_menu_widget):
    def __init__(self, main_page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.main_page = main_page

        self.setupButtons()
        self.attach()

    def setupButtons(self): pass

    def attach(self): pass
