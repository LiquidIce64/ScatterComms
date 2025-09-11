from typing import Optional

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, QMimeData, QPointF
from PySide6.QtGui import QDrag, QPixmap


class DraggableWidget(QWidget):
    drop_actions = Qt.DropAction.IgnoreAction

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allow_drag = True
        self.__drag_start_pos = QPointF()

    def drag_render_widget(self) -> Optional[QWidget]: return self
    def init_mime(self, mime: QMimeData): pass

    def drag_start(self):
        self.window().setFocus()
        self.hide()

    def drag_end(self): self.show()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.__drag_start_pos = event.position()

    def mouseMoveEvent(self, event):
        if self.allow_drag and event.buttons() == Qt.MouseButton.LeftButton:
            drag_vector = (event.position() - self.__drag_start_pos)
            if max(abs(drag_vector.x()), abs(drag_vector.y())) < QApplication.startDragDistance():
                return
            drag = QDrag(self)
            mime = QMimeData()
            self.init_mime(mime)
            drag.setMimeData(mime)

            render_widget = self.drag_render_widget()
            if render_widget is not None:
                p_ratio = render_widget.devicePixelRatio()
                size = render_widget.size() * p_ratio
                # Small drag pixmaps get rendered incorrectly on HDR displays.
                # Setting a pixmap size above 255 forces it to draw a proper color-corrected window
                # instead of doing cursor image shenanigans...
                pixmap = QPixmap(max(size.width(), 256), size.height())
                pixmap.setDevicePixelRatio(p_ratio)
                pixmap.fill(Qt.GlobalColor.transparent)
                render_widget.render(pixmap, renderFlags=QWidget.RenderFlag.DrawChildren)
                drag.setPixmap(pixmap)

            self.drag_start()
            drag.exec(self.drop_actions)
            self.drag_end()
