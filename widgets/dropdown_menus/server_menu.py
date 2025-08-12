from .menu_widget import MenuButton, MenuWidget


class ServerMenu(MenuWidget):
    def setupButtons(self):
        self.btn_test = MenuButton("test")
        self.layout_menu.addWidget(self.btn_test)
        self.btn_test2 = MenuButton("test2")
        self.layout_menu.addWidget(self.btn_test2)

    def attach(self):
        self.main_page.layout_main_page.addWidget(self, 1, 1, 1, 1)
        self.main_page.btn_server_title.setFocusProxy(self)

    def focusOutEvent(self, event):
        self.main_page.btn_server_title.btn.setChecked(False)
