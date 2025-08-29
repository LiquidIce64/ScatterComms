from .menu_widget import MenuWidget


class ServerMenu(MenuWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.btn_test = self.add_button('test')
        self.btn_test2 = self.add_button('test2')
