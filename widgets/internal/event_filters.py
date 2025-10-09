from PySide6.QtCore import QObject, Signal, QEvent
from PySide6.QtGui import QMouseEvent, QEnterEvent, QKeyEvent


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


class KeyEventFilter(QObject):
    keyPressed = Signal(QKeyEvent)
    keyReleased = Signal(QKeyEvent)

    def eventFilter(self, watched, event):
        if event.type() == event.Type.KeyPress:
            self.keyPressed.emit(event)
        elif event.type() == event.Type.KeyRelease:
            self.keyReleased.emit(event)
        return super().eventFilter(watched, event)
