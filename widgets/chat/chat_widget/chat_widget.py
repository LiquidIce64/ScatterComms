from PySide6.QtCore import Qt

from .ui_chat_widget import Ui_chat_widget
from widgets.common import DraggableWidget
from resources import Icons
from backend import ChatBackend, ConfigBackend


class ChatWidget(DraggableWidget, Ui_chat_widget):
    drop_actions = Qt.DropAction.MoveAction

    def __init__(self, chat: ChatBackend.Chat, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.icon.setIcon(Icons.TextChat, override_color=True)
        self.btn_settings.setIcon(Icons.Settings)

        self.chat = chat
        self.update_chat_info()
        self.chat.changed.connect(self.update_chat_info)
        server = ConfigBackend.session.selected_server
        if self.chat.uuid == server.selected_chat_uuid:
            server.selected_chat_changed.connect(self.on_deselect)
        self.update_highlight()

        self.btn.focused.connect(self.update_highlight)
        self.btn.focusLost.connect(self.update_highlight)
        self.btn.hovered.connect(self.update_highlight)
        self.btn.hoverEnd.connect(self.update_highlight)
        self.btn.clicked.connect(self.on_click)

    def update_chat_info(self):
        self.label.setText(self.chat.name)

    def on_click(self):
        server = ConfigBackend.session.selected_server
        server.selected_chat_uuid = self.chat.uuid
        server.selected_chat_changed.connect(self.on_deselect)
        self.update_highlight()

    def on_deselect(self):
        ConfigBackend.session.selected_server.selected_chat_changed.disconnect(self.on_deselect)
        self.update_highlight()

    def update_highlight(self):
        selected = (self.chat.uuid == ConfigBackend.session.selected_server.selected_chat_uuid)
        highlight = self.btn.hasFocus() or self.btn.underMouse()
        self.btn.setProperty('checked', selected)
        self.btn.style().polish(self.btn)
        self.label.setProperty('highlight', selected or highlight)
        self.label.style().polish(self.label)
        self.icon.setProperty('highlight', selected)
        self.icon.style().polish(self.icon)
        self.frame_buttons.setHidden(not highlight)
