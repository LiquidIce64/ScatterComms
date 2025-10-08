from PySide6.QtCore import QObject, Signal, QEvent
from PySide6.QtGui import QMouseEvent, QEnterEvent


class HoverEventFilter(QObject):
    hoverEnter = Signal(QEnterEvent)
    hoverLeave = Signal(QEvent)

    def eventFilter(self, watched, event):
        if event.type() == event.Type.Enter:
            self.hoverEnter.emit(event)
        elif event.type() == event.Type.Leave:
            self.hoverLeave.emit(event)
        return super().eventFilter(watched, event)


class MouseClickEventFilter(QObject):
    pressed = Signal(QMouseEvent)
    released = Signal(QMouseEvent)

    def eventFilter(self, watched, event):
        if event.type() == event.Type.MouseButtonPress:
            self.pressed.emit(event)
        elif event.type() == event.Type.MouseButtonRelease:
            self.released.emit(event)
        return super().eventFilter(watched, event)
