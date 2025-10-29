from PySide6.QtWidgets import QLabel, QPushButton
from PySide6.QtCore import QRect, Qt, QPoint
from PySide6.QtGui import QIcon, QPainter, QPaintEvent, QPixmap


def draw_colored_icon(painter: QPainter, icon: QIcon, rect: QRect):
    p_ratio = painter.device().devicePixelRatio()
    pixmap = QPixmap(rect.size() * p_ratio)
    pixmap.setDevicePixelRatio(p_ratio)
    pixmap.fill(Qt.GlobalColor.transparent)

    icon_painter = QPainter(pixmap)
    icon.paint(icon_painter, QRect(QPoint(), rect.size()))
    icon_painter.setCompositionMode(icon_painter.CompositionMode.CompositionMode_SourceIn)
    icon_painter.fillRect(pixmap.rect(), painter.pen().color())
    icon_painter.end()

    painter.drawPixmap(rect.topLeft(), pixmap)


class IconWidget(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__icon: QIcon | None = None
        self.__override_color = False

    def setIcon(self, icon: QIcon, override_color=False):
        self.__icon = icon
        self.__override_color = override_color
        self.update()

    def setPixmap(self, pixmap):
        self.setIcon(QIcon(pixmap))

    def icon(self):
        return self.__icon

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        self.initPainter(painter)
        if self.__icon is not None:
            if self.__override_color:
                draw_colored_icon(painter, self.__icon, self.contentsRect())
            else:
                self.__icon.paint(painter, self.contentsRect())
        painter.end()


class IconButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__icon: QIcon | None = None
        self.toggled.connect(self.update_highlight)

    def setIcon(self, icon):
        self.__icon = icon
        self.update()

    def update_highlight(self):
        self.setProperty('highlight', self.isChecked() or self.hasFocus() or self.underMouse())
        self.style().polish(self)

    def enterEvent(self, event): self.update_highlight()
    def leaveEvent(self, event): self.update_highlight()
    def focusInEvent(self, event): self.update_highlight()
    def focusOutEvent(self, event): self.update_highlight()

    def paintEvent(self, event: QPaintEvent):
        super().paintEvent(event)
        painter = QPainter(self)
        self.initPainter(painter)
        icon_rect = QRect()
        icon_rect.setSize(self.iconSize())
        icon_rect.moveCenter(self.rect().center())
        draw_colored_icon(painter, self.__icon, icon_rect)
        painter.end()
