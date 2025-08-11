from PySide6.QtWidgets import QWidget

from .ui_main_page import Ui_main_page
from widgets.chat_widget import ChatWidget, ServerChat
from widgets.vc_info import VCInfo
from widgets.search_widget import SearchWidget
from widgets.dropdown_menus import ServerMenu, ProfileMenu
from widgets.dropdown_menus.menu_widget import MenuWidget


class MainPage(QWidget, Ui_main_page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.search_widget = SearchWidget(self)
        self.layout_main_page.addWidget(self.search_widget, 1, 3, 2, 1)
        self.btn_search.clicked.connect(self.search_widget.toggle)

        self.dropdown_menu: MenuWidget | None = None
        self.btn_server_title.clicked.connect(lambda _: self.toggle_dropdown_menu(ServerMenu))
        self.btn_profile.clicked.connect(lambda _: self.toggle_dropdown_menu(ProfileMenu))
        self.btn_profile.clicked.connect(self.search_widget.hide)

        # debug
        self.chat_widget = ServerChat()
        self.layout_center_panel.addWidget(self.chat_widget)
        self.chat_widget.lower()
        self.vc_info = VCInfo(self)

    def toggle_dropdown_menu(self, menu_class):
        if self.dropdown_menu is not None:
            self.dropdown_menu.deleteLater()
            if isinstance(self.dropdown_menu, menu_class):
                self.dropdown_menu = None
                return
        self.dropdown_menu = menu_class(self)
