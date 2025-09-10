from PySide6.QtCore import Qt

from .ui_chat_category import Ui_chat_category_widget
from widgets.common import DraggableWidget
from resources import Icons


class ChatCategoryWidget(DraggableWidget, Ui_chat_category_widget):
    drop_actions = Qt.DropAction.MoveAction

    def __init__(self, category, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.category = category

        self.btn.setCheckable(True)
        self.btn.focused.connect(self.update_highlight)
        self.btn.focusLost.connect(self.update_highlight)
        self.btn.hovered.connect(self.update_highlight)
        self.btn.hoverEnd.connect(self.update_highlight)
        self.btn.toggled.connect(self.update_dropdown)

        self.update_dropdown()
        self.update_highlight()

    def drag_render_widget(self): return self.btn

    def update_dropdown(self):
        if self.btn.isChecked():
            self.icon_dropdown.setIcon(Icons.ArrowUp)
            self.frame_chats.show()
        else:
            self.icon_dropdown.setIcon(Icons.ArrowDown)
            self.frame_chats.hide()

    def update_highlight(self):
        self.label.setProperty('highlight', self.btn.isChecked() or self.btn.hasFocus() or self.btn.underMouse())
        self.label.style().polish(self.label)
