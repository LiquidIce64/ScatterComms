from typing import TYPE_CHECKING
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QCoreApplication, Qt

from .ui_main_page import Ui_main_page
from widgets.search_widget import SearchWidget
from widgets.dropdown_menus import MenuWidget, ServerMenu, ProfileMenu
from widgets.member import MemberCategoryWidget
from widgets.message import MessageWidget
from widgets.message.attachment import AttachmentPreview
from widgets.common import CustomScrollBar, AnchoredScrollBar
from resources import Icons
from backend import ProfileBackend, ConfigBackend, run_task, RoleBackend, MessageBackend

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
        self.update_server_title()
        ConfigBackend.session.server_changed.connect(self.update_server_title)

        # Profile
        self.btn_profile.setCheckable(True)
        self.btn_profile.toggled.connect(lambda: (
            self.btn_profile.isChecked() and (
                self.btn_search.setChecked(False),
                self.btn_server_title.setChecked(False)
            ),
            self.update_dropdown_menu(ProfileMenu, self.btn_profile)
        ))
        self.update_profile()
        self.update_status()
        ConfigBackend.session.profile.changed.connect(self.update_profile)
        ConfigBackend.session.profile_changed.connect(self.update_status)
        self.icon_useravatar.painter_mask = self.icon_useravatar.AvatarMask(self.icon_userstatus.size())

        # Chat
        self.textbox.save_max_height()
        self.textbox.returnPressed.connect(self.send_message)
        self.textbox.textChanged.connect(self.update_send_btn)
        self.btn_attachment.setIcon(Icons.Plus)
        self.btn_emoji.setIcon(Icons.Emoji)
        self.btn_send.setIcon(Icons.Send)
        self.btn_send.clicked.connect(self.send_message)
        self.btn_attachment.clicked.connect(self.add_attachment)
        self.scroll_attachments.hide()
        self.on_server_changed()
        ConfigBackend.session.server_changed.connect(self.on_server_changed)

        # Scrollbars
        self.scroll_chatlist.setVerticalScrollBar(CustomScrollBar(
            Qt.Orientation.Vertical,
            parent=self.scroll_chatlist
        ))
        self.scroll_chat.setVerticalScrollBar(AnchoredScrollBar(
            self.scroll_chat,
            Qt.Orientation.Vertical
        ))
        self.scroll_members.setVerticalScrollBar(CustomScrollBar(
            Qt.Orientation.Vertical,
            parent=self.scroll_members
        ))
        self.scroll_attachments.setHorizontalScrollBar(CustomScrollBar(
            Qt.Orientation.Horizontal,
            parent=self.scroll_attachments
        ))

    def on_server_changed(self):
        self.update_chat()
        ConfigBackend.session.selected_server.selected_chat_changed.connect(self.update_chat)

    def update_chat(self):
        chat = ConfigBackend.session.selected_server.selected_chat
        if chat is None:
            return
        self.icon_chat.setIcon(Icons.TextChat, override_color=True)
        self.label_chatname.setText(chat.name)
        run_task(
            RoleBackend.get_chat_members, chat.uuid,
            result_slot=self.update_chat_members
        )
        run_task(
            MessageBackend.get_messages, chat.uuid,
            result_slot=self.update_chat_messages
        )

    def update_chat_messages(self, messages: list[MessageBackend.Message]):
        for i in range(self.layout_chat.count() - 1, -1, -1):
            w = self.layout_chat.itemAt(i).widget()
            if isinstance(w, MessageWidget):
                w.deleteLater()
        for message in messages:
            self.layout_chat.addWidget(MessageWidget(message))

    def update_chat_members(self, result):
        for i in range(self.layout_memberlist.count() - 1, -1, -1):
            w = self.layout_memberlist.itemAt(i).widget()
            if isinstance(w, MemberCategoryWidget):
                w.deleteLater()

        grouped_roles, ungrouped_members = result
        if ungrouped_members:
            online_category = MemberCategoryWidget(members=ungrouped_members)
            online_category.label_name.setText(QCoreApplication.translate('member_category', 'Online'))
            self.layout_memberlist.insertWidget(0, online_category)
        for role, role_members in grouped_roles[::-1]:
            self.layout_memberlist.insertWidget(0, MemberCategoryWidget(role, role_members))

    def update_server_title(self):
        server = ConfigBackend.session.selected_server
        if server is None:
            return
        name = server.name
        if name == 'Saved Messages':
            name = QCoreApplication.translate('main_page', 'Saved Messages')
        self.label_servername.setText(name)

    def update_profile(self):
        profile = ConfigBackend.session.profile
        self.label_username.setText(profile.username)
        self.icon_useravatar.setPixmap(profile.avatar or Icons.Avatar)

    def update_status(self):
        try:
            status_icon = getattr(Icons.Status, ConfigBackend.session.status.name)
        except Exception:
            status_icon = Icons.Status.Online
            ConfigBackend.session.status = ProfileBackend.Status.Online
        self.icon_userstatus.setIcon(status_icon)
        self.label_userstatus.setText(QCoreApplication.translate('main_page', ConfigBackend.session.status.value))

    def add_attachment(self):
        filepaths = QFileDialog.getOpenFileNames(
            parent=self,
            caption='Select file to attach'
        )[0]
        for filepath in filepaths:
            widget = AttachmentPreview(filepath, parent=self)
            widget.destroyed.connect(self.on_attachment_removed)
            if self.layout_attachments.count() == 1:
                self.scroll_attachments.show()
            self.layout_attachments.insertWidget(self.layout_attachments.count() - 1, widget)
        self.update_send_btn()

    def on_attachment_removed(self):
        if self.layout_attachments.count() == 2:
            self.scroll_attachments.hide()
        self.update_send_btn()

    def update_send_btn(self):
        has_text = not self.textbox.document().isEmpty()
        self.btn_send.setEnabled(has_text or self.layout_attachments.count() > 1)

    def send_message(self):
        message_text = self.textbox.document().toPlainText()
        self.textbox.clear()
        attachment_filepaths: list[str] = []
        for i in range(self.layout_attachments.count() - 1):
            w = self.layout_attachments.itemAt(i).widget()
            if isinstance(w, AttachmentPreview):
                attachment_filepaths.append(w.filepath)
                w.deleteLater()

        if message_text == '' and not attachment_filepaths:
            return
        session = ConfigBackend.session
        message = MessageBackend.create_message(
            session.selected_server.selected_chat.uuid,
            session.profile.uuid,
            message_text,
            attachment_filepaths
        )
        self.layout_chat.addWidget(MessageWidget(message))

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
            Icons.ArrowUp if self.btn_server_title.isChecked() else Icons.ArrowDown,
            override_color=True
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

    def deleteLater(self):
        ConfigBackend.session.server_changed.disconnect(self.update_server_title)
        ConfigBackend.session.profile.changed.disconnect(self.update_profile)
        ConfigBackend.session.profile_changed.disconnect(self.update_status)
        ConfigBackend.session.server_changed.disconnect(self.on_server_changed)
        for child in self.findChildren(QWidget):
            child.deleteLater()
        super().deleteLater()

    def __del__(self):
        print('[DEBUG] Main page deleted')
