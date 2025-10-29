from PySide6.QtCore import Qt

from .ui_server_widget import Ui_widget_server
from widgets.common import DraggableWidget, MenuWidget
from resources import Icons
from backend import ServerBackend, ConfigBackend


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
        if self.server == ConfigBackend.session.selected_server:
            ConfigBackend.session.server_changed.connect(self.on_server_change)

        self.notification = False

        self.update_line()

    def contextMenuEvent(self, event):
        menu = MenuWidget(parent=self, icons_on_left=False)

        menu.add_button('Server settings', Icons.Generic.Settings, 4, slot=self.server_settings)

        if self.server.name != 'Saved Messages':
            menu.addSeparator()
            menu.add_button('Leave server', Icons.Generic.Cross, 4, slot=self.leave_server, danger=True)

        menu.exec(event.globalPos())
        menu.deleteLater()

    def server_settings(self):
        pass

    def leave_server(self):
        pass

    def update_server_info(self):
        self.setToolTip(self.server.name)
        self.icon.setPixmap(self.server.icon or Icons.Server.Server)

    def drag_render_widget(self): return self.icon

    def update_line(self):
        if ConfigBackend.session and self.server == ConfigBackend.session.selected_server:
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
        ConfigBackend.session.selected_server = self.server
        ConfigBackend.session.server_changed.connect(self.on_server_change)
        self.update_line()

    def on_server_change(self):
        ConfigBackend.session.server_changed.disconnect(self.on_server_change)
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
