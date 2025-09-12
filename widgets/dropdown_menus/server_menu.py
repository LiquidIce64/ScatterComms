from .menu_widget import MenuWidget
from resources import Icons


class ServerMenu(MenuWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.btn_create_category = self.add_button('Create Category', Icons.Plus)

    def connect_button_signals(self, main_page):
        self.btn_create_category.clicked.connect(main_page.widget_chatlist.create_category)
