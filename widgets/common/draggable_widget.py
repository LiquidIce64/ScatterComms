from typing import Optional

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag, QPixmap


class DraggableWidget(QWidget):
    drop_actions = Qt.DropAction.IgnoreAction

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allow_drag = True

    def drag_render_widget(self) -> Optional[QWidget]: return self
    def init_mime(self, mime: QMimeData): pass

    def drag_start(self):
        self.window().setFocus()
        self.hide()

    def drag_end(self): self.show()

    def mouseMoveEvent(self, event):
        if self.allow_drag and event.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            self.init_mime(mime)
            drag.setMimeData(mime)

            render_widget = self.drag_render_widget()
            if render_widget is not None:
                p_ratio = render_widget.devicePixelRatio()
                pixmap = QPixmap(render_widget.size() * p_ratio)
                pixmap.setDevicePixelRatio(p_ratio)
                pixmap.fill(Qt.GlobalColor.transparent)
                render_widget.render(pixmap, renderFlags=QWidget.RenderFlag.DrawChildren)
                drag.setPixmap(pixmap)

            self.drag_start()
            drag.exec(self.drop_actions)
            self.drag_end()
