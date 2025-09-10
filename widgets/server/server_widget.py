from PySide6.QtCore import Qt

from .ui_server_widget import Ui_widget_server
from widgets.common import DraggableWidget
from resources import Icons
from backend import ServerBackend


class ServerWidget(DraggableWidget, Ui_widget_server):
    # noinspection PyTypeChecker
    drop_actions = Qt.DropAction.MoveAction | Qt.DropAction.LinkAction

    def __init__(self, server: ServerBackend.Server, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.icon.painter_mask = self.icon.RoundedRectMask()

        self.server = server
        self.update_server_info()
        self.server.changed.connect(self.update_server_info)

        self.selected = False
        self.notification = False

        self.update_line()

    def update_server_info(self):
        self.setToolTip(self.server.name)
        self.icon.setPixmap(self.server.icon or Icons.Server)

    def drag_render_widget(self): return self.icon

    def update_line(self):
        if self.selected:
            self.line.setFixedHeight(self.height())
            self.line.show()
        elif self.underMouse() or self.hasFocus():
            self.line.setFixedHeight(self.height() // 2)
            self.line.show()
        elif self.notification:
            self.line.setFixedHeight(4)
            self.line.show()
        else:
            self.line.hide()

    def click(self):
        self.selected = True
        self.update_line()

    def enterEvent(self, event): self.update_line()
    def leaveEvent(self, event): self.update_line()
    def focusInEvent(self, event): self.update_line()
    def focusOutEvent(self, event): self.update_line()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.click()

    def mouseReleaseEvent(self, event):
        if (
            event.button() == Qt.MouseButton.LeftButton
            and self.contentsRect().contains(event.position().toPoint())
        ):
            self.click()
