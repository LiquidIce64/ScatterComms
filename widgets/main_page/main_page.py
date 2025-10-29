from typing import TYPE_CHECKING
from PySide6.QtWidgets import QWidget, QFileDialog, QApplication
from PySide6.QtCore import QCoreApplication, Qt, QPoint

from .ui_main_page import Ui_main_page
from widgets.search_widget import SearchWidget
from widgets.member import MemberCategoryWidget
from widgets.message import MessageWidget
from widgets.message.attachment import AttachmentPreview
from widgets.common import CustomScrollBar, AnchoredScrollBar, MenuWidget
from resources import Icons
from backend import ProfileBackend, ConfigBackend, run_task, RoleBackend, MessageBackend

if TYPE_CHECKING:
    from widgets import MainWindow


class MainPage(QWidget, Ui_main_page):
    CHAT_PAGE_SIZE = 20
    CHAT_PAGE_LOAD_MARGIN = 150

    def __init__(self, main_window: 'MainWindow', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.main_window = main_window

        # Settings
        self.btn_settings.setIcon(Icons.Generic.Settings)

        # Search
        self.search_widget = SearchWidget(self)
        self.layout_main_page.addWidget(self.search_widget, 1, 3, 2, 1)
        self.btn_search.toggled.connect(lambda: (
            self.search_widget.toggle(),
            self.btn_search.isChecked() and self.btn_profile.setChecked(False)
        ))
        self.btn_search.setIcon(Icons.Generic.Search)

        # Server list
        self.frame_servers.scrolled.connect(self.scroll_servers.scroll)

        # Server title
        self.btn_server_title.setCheckable(True)
        self.icon_server_dropdown.setIcon(Icons.Generic.ArrowDown, override_color=True)
        self.btn_server_title.clicked.connect(self.server_menu)
        self.btn_server_title.customContextMenuRequested.connect(self.server_menu)

        # Profile
        self.btn_profile.setCheckable(True)
        self.btn_profile.clicked.connect(self.profile_menu)
        self.btn_profile.customContextMenuRequested.connect(self.profile_menu)
        self.update_profile()
        self.update_status()
        ConfigBackend.session.profile.changed.connect(self.update_profile)
        ConfigBackend.session.profile_changed.connect(self.update_status)
        self.icon_useravatar.painter_mask = self.icon_useravatar.AvatarMask(self.icon_userstatus.size())

        # Chat
        self.scrollbar_chat = AnchoredScrollBar(
            self.scroll_chat,
            Qt.Orientation.Vertical
        )
        self.scrollbar_chat.valueChanged.connect(self.on_chat_scroll)
        self.scrollbar_chat.sliderReleased.connect(self.on_chat_scroll)
        self.scroll_chat.setVerticalScrollBar(self.scrollbar_chat)
        self.chat_loading = True
        self.chat_more_above = False
        self.chat_more_below = False

        self.textbox.save_max_height()
        self.textbox.returnPressed.connect(self.send_message)
        self.textbox.textChanged.connect(self.update_send_btn)
        self.btn_attachment.setIcon(Icons.Generic.Plus)
        self.btn_emoji.setIcon(Icons.Message.Emoji)
        self.btn_send.setIcon(Icons.Message.Send)
        self.btn_send.clicked.connect(self.send_message)
        self.btn_attachment.clicked.connect(self.add_attachment)
        self.scroll_attachments.hide()
        self.on_server_changed()
        ConfigBackend.session.server_changed.connect(self.on_server_changed)

        self.scroll_chatlist.setVerticalScrollBar(CustomScrollBar(
            Qt.Orientation.Vertical,
            parent=self.scroll_chatlist
        ))
        self.scroll_members.setVerticalScrollBar(CustomScrollBar(
            Qt.Orientation.Vertical,
            parent=self.scroll_members
        ))
        self.scroll_attachments.setHorizontalScrollBar(CustomScrollBar(
            Qt.Orientation.Horizontal,
            parent=self.scroll_attachments
        ))

    def server_menu(self):
        self.btn_server_title.setChecked(True)
        self.icon_server_dropdown.setIcon(Icons.Generic.ArrowUp, override_color=True)
        menu = MenuWidget(parent=self, icons_on_left=False)

        menu.add_button('Create category', Icons.Generic.Plus, 4, slot=self.widget_chatlist.create_category)
        menu.addSeparator()
        menu.add_button('Server settings', Icons.Generic.Settings, 4, slot=self.server_settings)

        if ConfigBackend.session.selected_server.name != 'Saved Messages':
            menu.addSeparator()
            menu.add_button('Leave server', Icons.Generic.Cross, 4, slot=self.leave_server, danger=True)

        pos = self.mapToGlobal(self.btn_server_title.geometry().bottomLeft())
        pos += QPoint(4, 5)
        menu.setFixedWidth(self.btn_server_title.width() - 7)

        menu.exec(pos)
        menu.deleteLater()

        self.btn_server_title.setChecked(False)
        self.icon_server_dropdown.setIcon(Icons.Generic.ArrowDown, override_color=True)

    def server_settings(self):
        pass

    def leave_server(self):
        pass

    def profile_menu(self):
        self.btn_profile.setChecked(True)
        menu = MenuWidget(parent=self)

        def add_status_button(name, icon, status):
            def set_status():
                ConfigBackend.session.status = status
            btn, action = menu.add_button(name, icon, override_icon_color=False, slot=set_status)
            btn.icon.setStyleSheet('''
                #btn_icon {
                    margin: 4px;
                    padding: 2px;
                    background-color: #303030;
                    border-radius: 8px;
                }
            ''')

        add_status_button('Online', Icons.Status.Online, ProfileBackend.Status.Online)
        add_status_button('Away', Icons.Status.Away, ProfileBackend.Status.Away)
        add_status_button('Do not disturb', Icons.Status.DoNotDisturb, ProfileBackend.Status.DoNotDisturb)
        add_status_button('Invisible', Icons.Status.Offline, ProfileBackend.Status.Offline)
        menu.addSeparator()
        menu.add_button('Edit profile', Icons.Generic.Edit, 4, slot=self.edit_profile)
        _, profile_action = menu.add_button('Change profile', Icons.Profile.User, 4, slot=self.change_profile)

        pos = self.mapToGlobal(self.frame_controls.geometry().bottomLeft())
        pos += QPoint(4, 5)
        menu.setFixedWidth(self.frame_controls.width() - 7)

        selected = menu.exec(pos)
        menu.deleteLater()

        if selected != profile_action:
            self.btn_profile.setChecked(False)

    def edit_profile(self):
        pass

    def change_profile(self):
        self.main_window.switch_to(self.main_window.Page.Profiles)

    def on_server_changed(self):
        self.update_server_title()
        self.update_chat()
        ConfigBackend.session.selected_server.selected_chat_changed.connect(self.update_chat)

    def clear_chat(self):
        self.scrollbar_chat.clear_anchor()
        for i in range(self.layout_chat.count() - 1, -1, -1):
            w = self.layout_chat.itemAt(i).widget()
            if isinstance(w, MessageWidget):
                w.deleteLater()

    def update_chat(self):
        self.clear_chat()
        chat = ConfigBackend.session.selected_server.selected_chat
        if chat is None:
            return
        self.icon_chat.setIcon(Icons.Server.TextChat, override_color=True)
        self.label_chatname.setText(chat.name)
        run_task(
            RoleBackend.get_chat_members, chat.uuid,
            result_slot=self.update_chat_members
        )
        self.chat_loading = True
        run_task(
            MessageBackend.get_messages, chat.uuid, self.CHAT_PAGE_SIZE,
            result_slot=self.reload_messages
        )

    def on_chat_scroll(self, *_):
        if self.chat_loading or self.scrollbar_chat.isSliderDown():
            return
        chat = ConfigBackend.session.selected_server.selected_chat
        if chat is None:
            return
        new_value = self.scrollbar_chat.value()

        if self.chat_more_above and new_value <= self.scrollbar_chat.minimum() + self.CHAT_PAGE_LOAD_MARGIN:
            widget = self.layout_chat.itemAt(1).widget()
            if not isinstance(widget, MessageWidget):
                return
            self.chat_loading = True
            run_task(
                MessageBackend.get_messages, chat.uuid, self.CHAT_PAGE_SIZE,
                before=widget.message.created_at_utc,
                result_slot=self.insert_messages,
            )
            return

        if self.chat_more_below and new_value >= self.scrollbar_chat.maximum() - self.CHAT_PAGE_LOAD_MARGIN:
            widget = self.layout_chat.itemAt(self.layout_chat.count() - 1).widget()
            if not isinstance(widget, MessageWidget):
                return
            self.chat_loading = True
            run_task(
                MessageBackend.get_messages, chat.uuid, self.CHAT_PAGE_SIZE,
                after=widget.message.created_at_utc,
                result_slot=self.add_messages,
            )
            return

    def add_messages(self, messages: list[MessageBackend.Message], /, detach=True):
        self.chat_more_below = len(messages) == self.CHAT_PAGE_SIZE
        self.chat_loading = False
        del_count = max(0, self.layout_chat.count() - 1 + len(messages) - self.CHAT_PAGE_SIZE * 3)
        if del_count > 0:
            self.chat_more_above = True

        for message in messages:
            self.layout_chat.addWidget(MessageWidget(message))

        for _ in range(del_count):
            self.layout_chat.takeAt(1).widget().deleteLater()

        if detach:
            self.scrollbar_chat.detach_from_bottom()
        self.scrollbar_chat.queue_update()

    def insert_messages(self, messages: list[MessageBackend.Message]):
        self.chat_more_above = len(messages) == self.CHAT_PAGE_SIZE
        self.chat_loading = False
        del_count = max(0, self.layout_chat.count() - 1 + len(messages) - self.CHAT_PAGE_SIZE * 3)
        if del_count > 0:
            self.chat_more_below = True

        for message in messages:
            self.layout_chat.insertWidget(1, MessageWidget(message))

        for _ in range(del_count):
            self.layout_chat.takeAt(self.layout_chat.count() - 1).widget().deleteLater()

        self.scrollbar_chat.queue_update()

    def reload_messages(self, messages: list[MessageBackend.Message]):
        self.clear_chat()
        self.chat_more_below = False
        self.chat_more_above = len(messages) == self.CHAT_PAGE_SIZE
        for message in messages:
            self.layout_chat.insertWidget(1, MessageWidget(message))
        self.scrollbar_chat.setValue(self.scrollbar_chat.maximum())
        self.chat_loading = False

    def update_chat_members(self, grouped_roles: list[tuple[RoleBackend.Role | None, list[ProfileBackend.Profile]]]):
        for i in range(self.layout_memberlist.count() - 1, -1, -1):
            w = self.layout_memberlist.itemAt(i).widget()
            if isinstance(w, MemberCategoryWidget):
                w.deleteLater()

        for role, role_members in grouped_roles[::-1]:
            if role is not None:
                self.layout_memberlist.insertWidget(0, MemberCategoryWidget(role, role_members))
            else:
                online_category = MemberCategoryWidget(members=role_members)
                online_category.label_name.setText(QCoreApplication.translate('member_category', 'Online'))
                self.layout_memberlist.insertWidget(0, online_category)

    def update_server_title(self):
        server = ConfigBackend.session.selected_server
        if server is None:
            return
        name = server.name
        if name == 'Saved Messages':
            name = QCoreApplication.translate('main_page', 'Saved Messages')
        self.label_servername.setText(name)
        self.label_servername.setToolTip(name)

    def update_profile(self):
        profile = ConfigBackend.session.profile
        self.label_username.setText(profile.username)
        self.icon_useravatar.setPixmap(profile.avatar or Icons.Profile.Avatar)

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
            caption=QApplication.translate('file_dialog', 'Attach file')
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
        self.btn_send.setEnabled(has_text or self.scroll_attachments.isVisible())

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
        chat_uuid = session.selected_server.selected_chat.uuid
        message = MessageBackend.create_message(
            chat_uuid,
            session.profile.uuid,
            message_text,
            attachment_filepaths
        )
        if self.chat_more_below:
            self.chat_loading = True
            run_task(
                MessageBackend.get_messages, chat_uuid, self.CHAT_PAGE_SIZE,
                result_slot=self.reload_messages
            )
        else:
            self.add_messages([message], detach=False)
            self.scrollbar_chat.setValue(self.scrollbar_chat.maximum())

    def deleteLater(self):
        ConfigBackend.session.profile.changed.disconnect(self.update_profile)
        ConfigBackend.session.profile_changed.disconnect(self.update_status)
        ConfigBackend.session.server_changed.disconnect(self.on_server_changed)
        for child in self.findChildren(QWidget):
            child.deleteLater()
        super().deleteLater()

    def __del__(self):
        print('[DEBUG] Main page deleted')
