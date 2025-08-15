from .menu_widget import MenuWidget


class ServerMenu(MenuWidget):
    def setupButtons(self):
        self.btn_test = self.add_button('test')
        self.btn_test2 = self.add_button('test2')

    def attach(self):
        self.main_page.layout_main_page.addWidget(self, 1, 1, 1, 1)
        self.main_page.btn_server_title.setFocusProxy(self)

    def focusOutEvent(self, event):
        self.main_page.btn_server_title.setChecked(False)
