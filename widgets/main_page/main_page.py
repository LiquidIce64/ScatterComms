from PySide6.QtWidgets import QWidget

from .ui_main_page import Ui_main_page
from widgets.vc_info import VCInfo
from widgets.search_widget import SearchWidget
from widgets.dropdown_menus import ServerMenu, ProfileMenu
from widgets.dropdown_menus.menu_widget import MenuWidget
from resources import Icons


class MainPage(QWidget, Ui_main_page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.dropdown_menu: MenuWidget | None = None

        # Settings
        self.btn_settings.setIcon(Icons.settings)

        # Search
        self.search_widget = SearchWidget(self)
        self.layout_main_page.addWidget(self.search_widget, 1, 3, 2, 1)
        self.btn_search.toggled.connect(lambda: (
            self.search_widget.toggle(),
            self.btn_search.isChecked() and self.btn_profile.setChecked(False)
        ))
        self.btn_search.setIcon(Icons.search)

        # Server title
        self.update_server_dropdown_icon()
        self.btn_server_title.setCheckable(True)
        self.btn_server_title.toggled.connect(lambda: (
            self.btn_server_title.isChecked() and self.btn_profile.setChecked(False),
            self.update_dropdown_menu(ServerMenu, self.btn_server_title),
            self.update_server_dropdown_icon()
        ))

        # Profile
        self.btn_profile.setCheckable(True)
        self.btn_profile.toggled.connect(lambda: (
            self.btn_profile.isChecked() and (
                self.btn_search.setChecked(False),
                self.btn_server_title.setChecked(False)
            ),
            self.update_dropdown_menu(ProfileMenu, self.btn_profile)
        ))
        self.icon_userstatus.setIcon(Icons.Status.online)

        # Chat
        self.max_textbox_height = self.textbox.maximumHeight()
        self.textbox.document().documentLayout().documentSizeChanged.connect(self.update_textbox_height)
        self.textbox.textChanged.connect(lambda: (
            self.btn_send.setEnabled(not self.textbox.document().isEmpty())
        ))
        self.btn_attachment.setIcon(Icons.plus)
        self.btn_emoji.setIcon(Icons.emoji)
        self.btn_send.setIcon(Icons.send)

        # debug
        self.vc_info = VCInfo(self)

    def update_textbox_height(self):
        new_height = self.textbox.document().size().height()
        new_height = min(new_height, self.max_textbox_height)
        new_height = max(new_height, self.textbox.minimumHeight())
        self.textbox.setMaximumHeight(new_height)

    def update_dropdown_menu(self, menu_class, button):
        if button.isChecked():
            if not isinstance(self.dropdown_menu, menu_class):
                self.dropdown_menu = menu_class(self)
        elif isinstance(self.dropdown_menu, menu_class):
            self.dropdown_menu.deleteLater()
            self.dropdown_menu = None

    def update_server_dropdown_icon(self):
        self.icon_server_dropdown.setIcon(
            Icons.arrow_up if self.btn_server_title.isChecked() else Icons.arrow_down
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
                self.dropdown_menu.clearFocus()
                self.btn_server_title.setChecked(False)
                self.btn_profile.setChecked(False)

        super().mousePressEvent(event)
