from PySide6.QtWidgets import QFrame, QInputDialog
from PySide6.QtCore import Qt, QPointF

from .ui_chat_category import Ui_chat_category_widget
from widgets.common import DraggableWidget, MenuWidget
from widgets.internal import ContextMenuEventFilter
from widgets.chat.chat_widget import ChatWidget
from resources import Icons
from backend import run_task, ChatBackend, ConfigBackend


class ChatCategoryWidget(DraggableWidget, Ui_chat_category_widget):
    drop_actions = Qt.DropAction.MoveAction

    def __init__(self, category: ChatBackend.Category, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.btn_settings.setIcon(Icons.Settings)
        self.btn_create_chat.setIcon(Icons.Plus)

        self.drop_target = QFrame()
        self.drop_target.setObjectName('drop_target')
        self.drop_target.setFixedHeight(30)

        self.btn.setCheckable(True)

        self.category = category
        self.update_category_info()
        self.update_dropdown()
        self.update_highlight()

        self.category.changed.connect(self.update_category_info)
        self.btn.focused.connect(self.update_highlight)
        self.btn.focusLost.connect(self.update_highlight)
        self.btn.hovered.connect(self.update_highlight)
        self.btn.hoverEnd.connect(self.update_highlight)
        self.btn.toggled.connect(self.update_dropdown)

        self.btn_create_chat.clicked.connect(self.create_chat)
        self.btn_settings.clicked.connect(self.category_settings)

        event_filter = ContextMenuEventFilter(parent=self)
        event_filter.triggered.connect(self.contextMenuEvent)
        self.btn.installEventFilter(event_filter)

        run_task(
            ChatBackend.get_chats,
            ConfigBackend.session.profile.uuid,
            category.uuid,
            result_slot=self.add_chats
        )

    def contextMenuEvent(self, event):
        menu = MenuWidget(parent=self, icons_on_left=False)

        menu.add_button('Create chat', Icons.Plus, 4, slot=self.create_chat)
        menu.addSeparator()
        menu.add_button('Category settings', Icons.Settings, 4, slot=self.category_settings)
        menu.addSeparator()
        menu.add_button('Delete category', Icons.Cross, 4, slot=self.delete_category, danger=True)

        menu.exec(event.globalPos())
        menu.deleteLater()

    def category_settings(self):
        pass

    def delete_category(self):
        pass

    def add_chat(self, chat: ChatBackend.Chat, index=-1):
        widget = ChatWidget(chat, parent=self)
        if index == -1:
            self.layout_chats.addWidget(widget)
        else:
            self.layout_chats.insertWidget(index, widget)

    def add_chats(self, chats):
        for chat in chats:
            self.add_chat(chat)

    def create_chat(self):
        while True:
            name, ok = QInputDialog.getText(self, 'Create new chat', 'Chat name:')
            if not ok:
                return
            if name:
                break
        category = ChatBackend.create_chat(self.category.uuid, name)
        self.add_chat(category)

    def update_category_info(self):
        category_name = self.category.name
        self.label.setText(category_name)
        self.label.setToolTip(category_name)
        self.btn.setChecked(not self.category.collapsed)

    def drag_render_widget(self): return self.btn

    def update_dropdown(self):
        if self.btn.isChecked():
            self.icon_dropdown.setIcon(Icons.ArrowUp, override_color=True)
            self.frame_chats.show()
            self.category.collapsed = False
        else:
            self.icon_dropdown.setIcon(Icons.ArrowDown, override_color=True)
            self.frame_chats.hide()
            self.category.collapsed = True

    def update_highlight(self):
        highlight = self.btn.hasFocus() or self.btn.underMouse()
        self.label.setProperty('highlight', highlight)
        self.label.style().polish(self.label)
        self.icon_dropdown.setProperty('highlight', highlight)
        self.icon_dropdown.style().polish(self.icon_dropdown)
        self.frame_buttons.setHidden(not highlight)

    def mouseMoveEvent(self, event):
        if self.btn.underMouse():
            super().mouseMoveEvent(event)

    def dragEnterEvent(self, event):
        if not event.possibleActions() & Qt.DropAction.MoveAction:
            return
        widget = event.source()
        if not isinstance(widget, ChatWidget):
            return
        event.setDropAction(Qt.DropAction.MoveAction)
        event.accept()

    def dragLeaveEvent(self, event):
        self.drop_target.hide()

    def __drop_location(self, position: QPointF):
        y_pos = self.frame_chats.mapFrom(self, position).y()
        spacing = self.layout_chats.spacing() / 2
        widget_count = self.layout_chats.count()
        for i in range(widget_count):
            widget = self.layout_chats.itemAt(i).widget()
            if y_pos <= widget.geometry().bottom() + spacing:
                return i
        return widget_count

    def dragMoveEvent(self, event):
        self.layout_chats.insertWidget(self.__drop_location(event.position()), self.drop_target)
        self.drop_target.show()
        event.accept()

    def dropEvent(self, event):
        self.drop_target.hide()
        widget = event.source()
        if not isinstance(widget, ChatWidget):
            return
        self.layout_chats.insertWidget(self.__drop_location(event.position()), widget)
        chats = []
        for i in range(self.layout_chats.count()):
            w = self.layout_chats.itemAt(i).widget()
            if isinstance(w, ChatWidget):
                chats.append(w.chat.uuid)
        ChatBackend.reorder_chat_list(self.category.uuid, chats)
