from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent, QTextCharFormat

from .custom_scrollbar import CustomScrollBar


class MessageTextbox(QTextEdit):
    returnPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._max_textbox_height = 150
        self.document().documentLayout().documentSizeChanged.connect(self.update_textbox_height)
        self.setVerticalScrollBar(CustomScrollBar(Qt.Orientation.Vertical, parent=self))

    def keyPressEvent(self, event: QKeyEvent):
        self.setFontPointSize(11)  # Messy fix for random size reset on empty text (yeah idk either)

        if event.key() == Qt.Key.Key_Return and not (event.modifiers() & Qt.KeyboardModifier.ShiftModifier):
            self.returnPressed.emit()
        else:
            super().keyPressEvent(event)

    def save_max_height(self):
        self._max_textbox_height = self.maximumHeight()

    def update_textbox_height(self):
        new_height = self.document().size().height()
        new_height = min(new_height, self._max_textbox_height)
        new_height = max(new_height, self.minimumHeight())
        self.setMaximumHeight(int(new_height))
