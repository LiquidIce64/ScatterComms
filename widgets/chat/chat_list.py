from PySide6.QtWidgets import (
    QWidget, QFrame, QVBoxLayout,
    QSpacerItem, QSizePolicy, QInputDialog
)
from PySide6.QtCore import Qt, QPointF

from .chat_category import ChatCategoryWidget
from backend import ConfigBackend, run_task, ChatBackend


class ChatList(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.layout_chatlist = QVBoxLayout(self)
        self.layout_chatlist.setObjectName('layout_chatlist')
        self.layout_chatlist.setContentsMargins(6, 0, 6, 0)
        self.layout_chatlist.setSpacing(12)

        self.drop_target = QFrame()
        self.drop_target.setObjectName('drop_target')
        self.drop_target.setFixedHeight(24)

        self.spacer_chatlist = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.layout_chatlist.addSpacerItem(self.spacer_chatlist)

        self.reload_contents()
        ConfigBackend.session.server_changed.connect(self.reload_contents)

    def reload_contents(self):
        run_task(
            ChatBackend.get_categories,
            ConfigBackend.session.profile.uuid,
            ConfigBackend.session.selected_server.uuid,
            result_slot=self.add_categories
        )

    def add_category(self, category: ChatBackend.Category, index=-1):
        widget = ChatCategoryWidget(category, parent=self)
        if index == -1:
            index = self.layout_chatlist.count() - 1
        self.layout_chatlist.insertWidget(index, widget)

    def add_categories(self, categories):
        for i in range(self.layout_chatlist.count() - 1, -1, -1):
            w = self.layout_chatlist.itemAt(i).widget()
            if isinstance(w, ChatCategoryWidget):
                w.deleteLater()
        for category in categories:
            self.add_category(category)

    def create_category(self):
        while True:
            name, ok = QInputDialog.getText(self, 'Create new category', 'Category name:')
            if not ok:
                return
            if name:
                break
        category = ChatBackend.create_category(ConfigBackend.session.selected_server.uuid, name)
        self.add_category(category)

    def drag_end(self): self.drop_target.hide()

    def dragLeaveEvent(self, event): self.drag_end()

    def dragEnterEvent(self, event):
        if not event.possibleActions() & Qt.DropAction.MoveAction:
            return
        widget = event.source()
        if not isinstance(widget, ChatCategoryWidget):
            return
        event.setDropAction(Qt.DropAction.MoveAction)
        event.accept()

    def __drop_location(self, position: QPointF):
        y_pos = position.y()
        widget_count = self.layout_chatlist.count()
        i_offset = 0
        for i in range(0, widget_count):
            widget = self.layout_chatlist.itemAt(i).widget()
            if not isinstance(widget, ChatCategoryWidget):
                i_offset += 1
                continue
            if y_pos <= widget.geometry().center().y():
                return i - i_offset
        return widget_count - i_offset

    def dragMoveEvent(self, event):
        self.layout_chatlist.insertWidget(self.__drop_location(event.position()), self.drop_target)
        self.drop_target.show()
        event.accept()

    def dropEvent(self, event):
        self.drag_end()
        widget = event.source()
        if not isinstance(widget, ChatCategoryWidget):
            return
        self.layout_chatlist.insertWidget(self.__drop_location(event.position()), widget)
        categories = []
        for i in range(self.layout_chatlist.count()):
            w = self.layout_chatlist.itemAt(i).widget()
            if isinstance(w, ChatCategoryWidget):
                categories.append(w.category.uuid)
        ChatBackend.reorder_category_list(ConfigBackend.session.selected_server.uuid, categories)
