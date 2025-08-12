from PySide6.QtWidgets import QFrame, QPushButton


class FrameButton(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.btn = QPushButton()

    def mouseReleaseEvent(self, event):
        self.setFocus()
        self.btn.click()
