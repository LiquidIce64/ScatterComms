from PySide6.QtWidgets import QFrame, QPushButton


class FrameButton(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.btn = QPushButton()
        self.btn.toggled.connect(self.repaint)

    def mouseReleaseEvent(self, event):
        self.setFocus()
        self.btn.click()
