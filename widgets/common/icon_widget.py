from PySide6.QtWidgets import QLabel, QGraphicsColorizeEffect
from PySide6.QtGui import QIcon, QPainter


class IconWidget(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__icon: QIcon | None = None
        self.__effect = QGraphicsColorizeEffect(self)
        self.__effect.setEnabled(False)
        self.setGraphicsEffect(self.__effect)

    def setIcon(self, icon: QIcon, override_color=False):
        self.__icon = icon
        self.__effect.setEnabled(override_color)
        self.update()

    def setPixmap(self, pixmap):
        self.setIcon(QIcon(pixmap))

    def icon(self):
        return self.__icon

    def paintEvent(self, event):
        painter = QPainter(self)
        self.initPainter(painter)
        self.__effect.setColor(painter.pen().color())
        if self.__icon is not None:
            self.__icon.paint(painter, self.contentsRect())
        painter.end()
