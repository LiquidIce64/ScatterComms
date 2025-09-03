from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPainter, QPainterPath


class RoundedImage(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.initPainter(painter)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addEllipse(self.rect())
        painter.setClipPath(path)

        painter.drawPixmap(self.rect(), self.pixmap())
        painter.end()
