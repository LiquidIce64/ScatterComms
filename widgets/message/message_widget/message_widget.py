from typing import cast

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGraphicsColorizeEffect, QLabel, QApplication
from PySide6.QtGui import QColor, QTextDocument

from .ui_message_widget import Ui_message_widget
from widgets.message.reply_widget import ReplyWidget
from widgets.message.attachment import get_attachment_widget, AttachmentWidget
from widgets.common import MenuWidget
from resources import Icons
from backend import MessageBackend


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
        self.update_role_info()
        self.profile.top_role_changed.connect(self.update_role_info)
        self.reload_contents()
        self.message.changed.connect(self.reload_contents)
        self.label_timestamp.setText(message.created_at.strftime('%H:%M %d.%m.%Y'))
        if (replying_to := message.replying_to) is not None:
            self.layout_reply.addWidget(ReplyWidget(replying_to))

    def contextMenuEvent(self, event):
        menu = MenuWidget(parent=self, icons_on_left=False)

        has_text = bool(self.message.text)
        if has_text:
            text_label = cast(QLabel, self.layout_contents.itemAt(0).widget())
            if text_label.hasSelectedText():
                selected_text = text_label.selectedText()
                menu.add_button(
                    'Copy', Icons.Generic.Copy, 4,
                    slot=lambda: QApplication.clipboard().setText(selected_text)
                )
                menu.addSeparator()

        menu.add_button('Reply', Icons.Message.Send, 4, slot=self.reply)
        menu.add_button('Forward', Icons.Message.Send, 4, slot=self.forward)
        menu.add_button('Pin message', Icons.Message.Pin, 4, slot=self.pin)
        menu.addSeparator()

        if has_text:
            menu.add_button('Copy text', Icons.Generic.Copy, 4, slot=self.copy_text)

        attachment_count = 0
        attachment_widget = None
        for i in range(self.layout_contents.count()):
            w = self.layout_contents.itemAt(i).widget()
            if not (isinstance(w, AttachmentWidget) and isinstance(w, QWidget)):
                continue
            attachment_widget = cast(AttachmentWidget, w)
            attachment_count += 1
            if w.underMouse():
                attachment_widget.context_menu_buttons(menu)
                break
        else:
            if attachment_count == 1:
                attachment_widget.context_menu_buttons(menu)

        menu.addSeparator()
        menu.add_button('Delete message', Icons.Generic.Cross, 4, slot=self.delete_message, danger=True)

        menu.exec(event.globalPos())
        menu.deleteLater()

    def reply(self):
        pass

    def forward(self):
        pass

    def pin(self):
        pass

    def copy_text(self):
        document = QTextDocument()
        document.setHtml(self.message.text)
        QApplication.clipboard().setText(document.toPlainText())

    def delete_message(self):
        pass

    def update_profile_info(self):
        self.icon_avatar.setPixmap(self.profile.avatar or Icons.Profile.Avatar)
        self.label_username.setText(self.profile.username)

    def update_role_info(self):
        if self.profile.top_role is None:
            self.role_color_effect.setColor(QColor.fromRgba(0xFF808080))
        else:
            self.role_color_effect.setColor(self.profile.top_role.color)

    def reload_contents(self):
        for i in range(self.layout_contents.count() - 1, -1, -1):
            w = self.layout_contents.itemAt(i).widget()
            if w is not None:
                w.deleteLater()

        text = self.message.text
        if text is not None:
            label_text = QLabel(
                text=self.message.text,
                parent=self,
                wordWrap=True,
                openExternalLinks=True,
                textInteractionFlags=Qt.TextInteractionFlag.TextBrowserInteraction
            )
            label_text.setObjectName('label_text')
            label_text.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
            self.layout_contents.addWidget(label_text)
        else:
            self.layout_contents.setContentsMargins(0, 6, 0, 0)

        for attachment in self.message.attachments:
            widget = get_attachment_widget(attachment)
            widget.setParent(self)
            self.layout_contents.addWidget(widget)

    def deleteLater(self):
        for i in range(self.layout_contents.count() - 1, -1, -1):
            w = self.layout_contents.itemAt(i).widget()
            if w is not None:
                w.deleteLater()
        super().deleteLater()
