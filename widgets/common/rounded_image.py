from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QPainter, QPainterPath


class RoundedImage(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target = None

    def setPixmap(self, pixmap: QPixmap):
        self.target = QPixmap(pixmap.size())
        self.target.fill(Qt.GlobalColor.transparent)

        painter = QPainter(self.target)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)

        radius = int(min(pixmap.width(), pixmap.height()) / 2)
        path = QPainterPath()
        path.addRoundedRect(pixmap.rect(), radius, radius)
        painter.setClipPath(path)

        painter.drawPixmap(0, 0, pixmap)
        super().setPixmap(self.target)
