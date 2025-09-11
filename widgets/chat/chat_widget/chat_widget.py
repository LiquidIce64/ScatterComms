from PySide6.QtCore import Qt

from widgets.common import DraggableWidget
from .ui_chat_widget import Ui_chat_widget


class ChatWidget(DraggableWidget, Ui_chat_widget):
    drop_actions = Qt.DropAction.MoveAction

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.btn.focused.connect(self.update_highlight)
        self.btn.focusLost.connect(self.update_highlight)
        self.btn.hovered.connect(self.update_highlight)
        self.btn.hoverEnd.connect(self.update_highlight)

    def update_highlight(self):
        self.label.setProperty('highlight', self.btn.hasFocus() or self.btn.underMouse())
        self.label.style().polish(self.label)
