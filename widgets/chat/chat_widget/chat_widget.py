from PySide6.QtCore import Qt

from .ui_chat_widget import Ui_chat_widget
from widgets.common import DraggableWidget, MenuWidget
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
        if self.chat == server.selected_chat:
            server.selected_chat_changed.connect(self.on_deselect)
        self.update_highlight()

        self.btn.focused.connect(self.update_highlight)
        self.btn.focusLost.connect(self.update_highlight)
        self.btn.hovered.connect(self.update_highlight)
        self.btn.hoverEnd.connect(self.update_highlight)
        self.btn.clicked.connect(self.on_click)
        self.btn_settings.clicked.connect(self.chat_settings)

    def update_chat_info(self):
        chat_name = self.chat.name
        self.label.setText(chat_name)
        self.label.setToolTip(chat_name)

    def on_click(self):
        server = ConfigBackend.session.selected_server
        server.selected_chat = self.chat
        server.selected_chat_changed.connect(self.on_deselect)
        self.update_highlight()

    def on_deselect(self):
        ConfigBackend.session.selected_server.selected_chat_changed.disconnect(self.on_deselect)
        self.update_highlight()

    def update_highlight(self):
        selected = (self.chat == ConfigBackend.session.selected_server.selected_chat)
        highlight = self.btn.hasFocus() or self.btn.underMouse()
        self.btn.setProperty('checked', selected)
        self.btn.style().polish(self.btn)
        self.label.setProperty('highlight', selected or highlight)
        self.label.style().polish(self.label)
        self.icon.setProperty('highlight', selected)
        self.icon.style().polish(self.icon)
        self.frame_buttons.setHidden(not highlight)

    def contextMenuEvent(self, event):
        menu = MenuWidget(parent=self, icons_on_left=False)

        menu.add_button('Chat settings', Icons.Settings, 4, slot=self.chat_settings)
        menu.addSeparator()
        menu.add_button('Delete chat', Icons.Cross, 4, slot=self.delete_chat, danger=True)

        menu.exec(event.globalPos())
        menu.deleteLater()

    def chat_settings(self):
        pass

    def delete_chat(self):
        pass
