from PySide6.QtWidgets import QFrame, QPushButton
from PySide6.QtCore import Qt, Signal, QEvent
from PySide6.QtGui import QFocusEvent, QEnterEvent


class FrameButton(QFrame):
    focused = Signal(QFocusEvent)
    focusLost = Signal(QFocusEvent)
    hovered = Signal(QEnterEvent)
    hoverEnd = Signal(QEvent)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__btn = QPushButton()
        self.clicked = self.__btn.clicked
        self.toggled = self.__btn.toggled

        self.toggled.connect(self.__on_toggle)

    def __on_toggle(self):
        self.setProperty('checked', self.__btn.isChecked())
        self.style().polish(self)

    def click(self): self.__btn.click()
    def toggle(self): self.__btn.toggle()
    def setChecked(self, checked: bool): self.__btn.setChecked(checked)
    def setCheckable(self, checkable: bool): self.__btn.setCheckable(checkable)
    def isChecked(self): return self.__btn.isChecked()

    def mouseReleaseEvent(self, event):
        if (
            event.button() == Qt.MouseButton.LeftButton
            and self.contentsRect().contains(event.position().toPoint())
        ):
            self.click()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.click()

    def focusInEvent(self, event):
        self.focused.emit(event)
        self.update()
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.focusLost.emit(event)
        self.update()
        super().focusOutEvent(event)

    def enterEvent(self, event):
        self.hovered.emit(event)
        self.update()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.hoverEnd.emit(event)
        self.update()
        super().leaveEvent(event)

    def deleteLater(self):
        self.__btn.deleteLater()
        self.__btn = None
        super().deleteLater()
