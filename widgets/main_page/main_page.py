from typing import TYPE_CHECKING
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QWheelEvent

from .ui_main_page import Ui_main_page
from widgets.vc_info import VCInfo
from widgets.search_widget import SearchWidget
from widgets.dropdown_menus import MenuWidget, ServerMenu, ProfileMenu
from resources import Icons
from backend import ProfileBackend

if TYPE_CHECKING:
    from widgets import MainWindow


class MainPage(QWidget, Ui_main_page):
    def __init__(self, main_window: 'MainWindow', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.main_window = main_window
        self.dropdown_menu: MenuWidget | None = None

        # Settings
        self.btn_settings.setIcon(Icons.Settings)

        # Search
        self.search_widget = SearchWidget(self)
        self.layout_main_page.addWidget(self.search_widget, 1, 3, 2, 1)
        self.btn_search.toggled.connect(lambda: (
            self.search_widget.toggle(),
            self.btn_search.isChecked() and self.btn_profile.setChecked(False)
        ))
        self.btn_search.setIcon(Icons.Search)

        # Server list
        self.frame_servers.scrolled.connect(self.scroll_servers.scroll)

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
        self.label_username.setText(self.main_window.session.profile.username)
        self.update_status()
        self.main_window.session.status_changed.connect(self.update_status)
        self.icon_useravatar.painter_mask = self.icon_useravatar.AvatarMask(self.icon_userstatus.size())

        # Chat
        self.max_textbox_height = self.textbox.maximumHeight()
        self.textbox.document().documentLayout().documentSizeChanged.connect(self.update_textbox_height)
        self.textbox.textChanged.connect(lambda: (
            self.btn_send.setEnabled(not self.textbox.document().isEmpty())
        ))
        self.btn_attachment.setIcon(Icons.Plus)
        self.btn_emoji.setIcon(Icons.Emoji)
        self.btn_send.setIcon(Icons.Send)

        # debug
        self.vc_info = VCInfo(self)

    def update_status(self):
        status = self.main_window.session.status
        try:
            status_icon = getattr(Icons.Status, status.name)
        except Exception:
            status_icon = Icons.Status.Online
            self.main_window.session.status = ProfileBackend.Status.Online
        self.icon_userstatus.setIcon(status_icon)
        self.label_userstatus.setText(QCoreApplication.translate('main_page', status.value))

    def update_textbox_height(self):
        new_height = self.textbox.document().size().height()
        new_height = min(new_height, self.max_textbox_height)
        new_height = max(new_height, self.textbox.minimumHeight())
        self.textbox.setMaximumHeight(new_height)

    def update_dropdown_menu(self, menu_class, button):
        if button.isChecked():
            if not isinstance(self.dropdown_menu, menu_class):
                self.dropdown_menu = menu_class(self)
                self.dropdown_menu.focusLost.connect(lambda e: button.setChecked(False))
                self.dropdown_menu.connect_button_signals(self)
                self.layout_main_page.addWidget(self.dropdown_menu, *self.dropdown_menu.grid_layout_args)
                button.setFocusProxy(self.dropdown_menu)
                self.dropdown_menu.setFocus()
        elif isinstance(self.dropdown_menu, menu_class):
            self.dropdown_menu.deleteLater()
            self.dropdown_menu = None

    def update_server_dropdown_icon(self):
        self.icon_server_dropdown.setIcon(
            Icons.ArrowUp if self.btn_server_title.isChecked() else Icons.ArrowDown
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
