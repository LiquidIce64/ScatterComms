from typing import Optional

from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QPainter, QPainterPath


class BaseMask:
    def apply(self, rect: QRect, path: QPainterPath): pass


class MaskedImage(QLabel):
    class CircleMask(BaseMask):
        def apply(self, rect: QRect, path: QPainterPath):
            path.addEllipse(rect)

    class AvatarMask(BaseMask):
        def __init__(self, status_icon_size: QSize):
            self.__status_icon_size = status_icon_size

        def apply(self, rect: QRect, path: QPainterPath):
            path.addEllipse(rect)
            status_rect = QRect(rect)
            status_rect.setSize(self.__status_icon_size)
            status_rect.moveBottomRight(rect.bottomRight())
            status_path = QPainterPath()
            status_path.addEllipse(status_rect)
            path -= status_path

    class RoundedRectMask(BaseMask):
        def apply(self, rect: QRect, path: QPainterPath):
            radius = min(rect.width(), rect.height()) // 4
            path.addRoundedRect(rect, radius, radius)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.painter_mask: Optional[BaseMask] = None

    def paintEvent(self, event):
        painter = QPainter(self)
        self.initPainter(painter)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)

        if self.painter_mask is not None:
            path = QPainterPath()
            self.painter_mask.apply(self.rect(), path)
            painter.setClipPath(path)

        painter.drawPixmap(self.rect(), self.pixmap())
        painter.end()
