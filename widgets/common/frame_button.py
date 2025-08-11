from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QMouseEvent


class FrameButton(QFrame):
    clicked = Signal(QMouseEvent)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.clicked.emit(event)
