from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Signal


class ScrollableFrame(QFrame):
    scrolled = Signal(int, int)

    def wheelEvent(self, event):
        delta = event.pixelDelta()
        self.scrolled.emit(delta.x(), delta.y())
