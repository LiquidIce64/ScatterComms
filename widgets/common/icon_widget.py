from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QIcon, QPainter


class IconWidget(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__icon: QIcon | None = None

    def setIcon(self, icon: QIcon):
        self.__icon = icon
        self.repaint()

    def setPixmap(self, pixmap):
        self.setIcon(QIcon(pixmap))

    def icon(self):
        return self.__icon

    def paintEvent(self, event):
        painter = QPainter(self)
        self.initPainter(painter)
        if self.__icon is not None:
            self.__icon.paint(painter, self.contentsRect())
        painter.end()
