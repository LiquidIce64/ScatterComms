from typing import Optional, Union

from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QPainter, QPainterPath, QPixmap, QImage, QIcon


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
        def __init__(self, radius: int = None):
            self.__radius = radius

        def apply(self, rect: QRect, path: QPainterPath):
            radius = self.__radius or min(rect.width(), rect.height()) // 4
            path.addRoundedRect(rect, radius, radius)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.painter_mask: Optional[BaseMask] = None
        self.__icon: Optional[QIcon] = None

    def setPixmap(self, pixmap: Union[QPixmap, QImage, QIcon]):
        if isinstance(pixmap, QIcon):
            self.__icon = pixmap
        else:
            self.__icon = None
            if isinstance(pixmap, QImage):
                pixmap = QPixmap(pixmap)
            super().setPixmap(pixmap)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.initPainter(painter)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)

        if self.painter_mask is not None:
            path = QPainterPath()
            self.painter_mask.apply(self.rect(), path)
            painter.setClipPath(path)

        if self.__icon is None:
            painter.drawPixmap(self.rect(), self.pixmap())
        else:
            self.__icon.paint(painter, self.contentsRect())
        painter.end()
