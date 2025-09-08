from random import randint

from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QPushButton,
    QSpacerItem, QSizePolicy, QInputDialog
)
from PySide6.QtCore import Qt, QPointF

from .server_widget import ServerWidget
from widgets.common import IconWidget
from resources import Icons
from backend import ServerBackend, run_task, ConfigBackend


class ServerListBase(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.layout_frame = QVBoxLayout(self)
        self.layout_frame.setObjectName('layout_frame')
        self.layout_frame.setContentsMargins(0, 0, 0, 0)
        self.layout_frame.setSpacing(6)

    def add_server(self, server: ServerBackend.Server, index=-1):
        state = randint(1, 3)
        widget = ServerWidget(server, parent=self)
        if state == 2:
            widget.notification = True
        if state == 3:
            widget.selected = True
        widget.update_line()
        if index == -1:
            self.layout_frame.addWidget(widget)
        else:
            self.layout_frame.insertWidget(index, widget)

    def drag_start(self): pass
    def drag_end(self): pass

    def dragLeaveEvent(self, event): self.drag_end()

    def dragEnterEvent(self, event):
        if not event.possibleActions() & Qt.DropAction.MoveAction:
            return
        widget = event.source()
        if not isinstance(widget, ServerWidget):
            return
        self.drag_start()
        event.setDropAction(Qt.DropAction.MoveAction)
        event.accept()


class ServerList(ServerListBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setProperty('drag', False)

        self.btn_create_server = QPushButton(self)
        self.btn_create_server.setObjectName('btn_create_server')
        self.btn_create_server.setIcon(Icons.Plus)
        self.btn_create_server.setFixedSize(40, 40)
        self.btn_create_server.clicked.connect(self.create_server)
        self.layout_frame.addWidget(self.btn_create_server, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.spacer_servers = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.layout_frame.addSpacerItem(self.spacer_servers)

        run_task(
            ServerBackend.get_server_list_unpinned,
            ConfigBackend.session.profile.uuid,
            result_slot=self.add_servers
        )

    def add_servers(self, servers):
        for server in servers:
            self.add_server(server, index=0)

    def create_server(self):
        while True:
            name, ok = QInputDialog.getText(self, 'Create new server', 'Server name:')
            if not ok:
                return
            if name:
                break
        server = ServerBackend.create_server(name, ConfigBackend.session.profile.uuid)
        self.add_server(server, index=0)

    def drag_start(self):
        self.setProperty('drag', True)
        self.style().polish(self)

    def drag_end(self):
        self.setProperty('drag', False)
        self.style().polish(self)

    def dropEvent(self, event):
        self.drag_end()
        widget = event.source()
        if not isinstance(widget, ServerWidget):
            return
        self.layout_frame.insertWidget(0, widget)
        ServerBackend.reorder_server(ConfigBackend.session.profile.uuid, widget.server.uuid, 0)


class PinnedServerList(ServerListBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.drop_target = IconWidget()
        self.drop_target.setIcon(Icons.ServerFrame)
        self.drop_target.setObjectName('drop_target')
        self.drop_target.setFixedSize(40, 40)

        run_task(
            ServerBackend.get_server_list_pinned,
            ConfigBackend.session.profile.uuid,
            result_slot=self.add_servers
        )

    def add_servers(self, servers):
        for server in servers:
            self.add_server(server)
        saved_messages = self.layout_frame.itemAt(0)
        if saved_messages is not None:
            saved_messages = saved_messages.widget()
        if isinstance(saved_messages, ServerWidget):
            saved_messages.allow_drag = False
            saved_messages.icon.setPixmap(Icons.Save)
            saved_messages.setObjectName('saved_messages')
            saved_messages.setToolTip('Saved Messages')
            ConfigBackend.session.selected_server = saved_messages.server

    def __drop_location(self, position: QPointF):
        y_pos = position.y()
        spacing = self.layout_frame.spacing() / 2
        widget_count = self.layout_frame.count()
        for i in range(1, widget_count):
            widget = self.layout_frame.itemAt(i).widget()
            if y_pos <= widget.geometry().bottom() + spacing:
                return i
        return widget_count

    def dragMoveEvent(self, event):
        self.layout_frame.insertWidget(
            self.__drop_location(event.position()),
            self.drop_target,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        self.drop_target.show()
        event.accept()

    def drag_end(self): self.drop_target.hide()

    def dropEvent(self, event):
        self.drag_end()
        widget = event.source()
        if not isinstance(widget, ServerWidget):
            return
        self.layout_frame.insertWidget(self.__drop_location(event.position()), widget)
        servers = []
        for i in range(self.layout_frame.count()):
            w = self.layout_frame.itemAt(i).widget()
            if isinstance(w, ServerWidget):
                servers.append(w.server.uuid)
        ServerBackend.reorder_server_list(ConfigBackend.session.profile.uuid, servers)
