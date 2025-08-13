from PySide6.QtWidgets import QWidget

from .ui_main_page import Ui_main_page
from widgets.chat_widget import ServerChat
from widgets.vc_info import VCInfo
from widgets.search_widget import SearchWidget
from widgets.dropdown_menus import ServerMenu, ProfileMenu
from widgets.dropdown_menus.menu_widget import MenuWidget
from resources import Icons, StatusIcons


class MainPage(QWidget, Ui_main_page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.search_widget = SearchWidget(self)
        self.layout_main_page.addWidget(self.search_widget, 1, 3, 2, 1)
        self.btn_search.toggled.connect(self.search_widget.toggle)

        self.dropdown_menu: MenuWidget | None = None

        self.update_server_dropdown_icon()
        self.btn_server_title.btn.setCheckable(True)
        self.btn_server_title.btn.toggled.connect(lambda: (
            self.btn_server_title.btn.isChecked() and self.btn_profile.btn.setChecked(False),
            self.update_dropdown_menu(ServerMenu, self.btn_server_title),
            self.update_server_dropdown_icon()
        ))

        self.btn_profile.btn.setCheckable(True)
        self.btn_profile.btn.toggled.connect(lambda: (
            self.btn_search.setChecked(False),
            self.btn_profile.btn.isChecked() and self.btn_server_title.btn.setChecked(False),
            self.update_dropdown_menu(ProfileMenu, self.btn_profile)
        ))
        self.icon_userstatus.setIcon(StatusIcons.online)

        # debug
        self.chat_widget = ServerChat()
        self.layout_center_panel.addWidget(self.chat_widget)
        self.chat_widget.lower()
        self.vc_info = VCInfo(self)

    def update_dropdown_menu(self, menu_class, button):
        if button.btn.isChecked():
            if not isinstance(self.dropdown_menu, menu_class):
                self.dropdown_menu = menu_class(self)
        elif isinstance(self.dropdown_menu, menu_class):
            self.dropdown_menu.deleteLater()
            self.dropdown_menu = None

    def update_server_dropdown_icon(self):
        self.icon_server_dropdown.setIcon(
            Icons.arrow_up if self.btn_server_title.btn.isChecked() else Icons.arrow_down
        )

    def mousePressEvent(self, event):
        if self.dropdown_menu is not None:
            def outside_widget(widget: QWidget):
                pos = widget.parent().mapFrom(self, event.pos())
                return not widget.geometry().contains(pos)

            if (
                outside_widget(self.btn_server_title)
                and outside_widget(self.btn_profile)
                and outside_widget(self.dropdown_menu.frame_menu)
            ):
                self.btn_server_title.btn.setChecked(False)
                self.btn_profile.btn.setChecked(False)

        super().mousePressEvent(event)
