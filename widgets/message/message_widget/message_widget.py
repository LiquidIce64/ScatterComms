from PySide6.QtWidgets import QWidget, QGraphicsColorizeEffect
from PySide6.QtGui import QColor

from .ui_message_widget import Ui_message_widget
from widgets.message.reply_widget import ReplyWidget
from widgets.message.message_contents import MessageContent, TextContent
from resources import Icons
from backend import MessageBackend, RoleBackend, ConfigBackend


class MessageWidget(QWidget, Ui_message_widget):
    def __init__(self, message: MessageBackend.Message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.icon_avatar.painter_mask = self.icon_avatar.CircleMask()
        self.role_color_effect = QGraphicsColorizeEffect(parent=self.label_username, color=QColor.fromRgba(0xFF808080))
        self.label_username.setGraphicsEffect(self.role_color_effect)

        self.message = message
        self.profile = message.author
        self.update_profile_info()
        self.profile.changed.connect(self.update_profile_info)
        self.reload_contents()
        self.message.changed.connect(self.reload_contents)
        self.label_timestamp.setText(message.created_at.strftime('%Y.%m.%d %H:%M'))
        if (replying_to := message.replying_to) is not None:
            self.layout_reply.addWidget(ReplyWidget(replying_to))

        self.role: RoleBackend.Role | None = None
        self.__connect_role(RoleBackend.get_top_role(self.profile.uuid, ConfigBackend.session.selected_server.uuid))

    def __connect_role(self, role: RoleBackend.Role | None):
        if role is None:
            return
        self.role = role
        self.update_role_info()
        role.changed.connect(self.update_role_info)

    def update_profile_info(self):
        self.icon_avatar.setPixmap(self.profile.avatar or Icons.Avatar)
        self.label_username.setText(self.profile.username)

    def update_role_info(self):
        self.role_color_effect.setColor(self.role.color)

    def reload_contents(self):
        for i in range(self.layout_contents.count() - 1, -1, -1):
            w = self.layout_contents.itemAt(i).widget()
            if isinstance(w, MessageContent):
                w.deleteLater()

        text = self.message.text
        if text is not None:
            self.layout_contents.addWidget(TextContent(self.message, parent=self))
