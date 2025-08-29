from PySide6.QtWidgets import QFrame, QPushButton
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFocusEvent


class FrameButton(QFrame):
    focusLost = Signal(QFocusEvent)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__btn = QPushButton()
        self.clicked = self.__btn.clicked
        self.toggled = self.__btn.toggled

        self.toggled.connect(self.repaint)

    def click(self): self.__btn.click()
    def toggle(self): self.__btn.toggle()
    def setChecked(self, checked: bool): self.__btn.setChecked(checked)
    def setCheckable(self, checkable: bool): self.__btn.setCheckable(checkable)
    def isChecked(self): return self.__btn.isChecked()

    def mouseReleaseEvent(self, event): self.click()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.click()

    def focusOutEvent(self, event):
        self.focusLost.emit(event)
        super().focusOutEvent(event)

    def deleteLater(self):
        self.__btn.deleteLater()
        self.__btn = None
        super().deleteLater()
