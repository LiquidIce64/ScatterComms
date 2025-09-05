from random import randint

from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, QPointF

from .server_widget import ServerWidget
from widgets.common import IconWidget
from resources import Icons


class ServerListBase(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.layout_frame = QVBoxLayout(self)
        self.layout_frame.setObjectName('layout_frame')
        self.layout_frame.setContentsMargins(0, 0, 0, 0)
        self.layout_frame.setSpacing(6)

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
        self.layout_frame.addWidget(self.btn_create_server, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.spacer_servers = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.layout_frame.addSpacerItem(self.spacer_servers)

        # debug
        def add_server():
            state = randint(1, 3)
            widget = ServerWidget(parent=self)
            if state == 2:
                widget.notification = True
            if state == 3:
                widget.selected = True
            widget.update_line()
            self.layout_frame.insertWidget(0, widget)
        self.btn_create_server.clicked.connect(add_server)

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


class PinnedServerList(ServerListBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.drop_target = IconWidget()
        self.drop_target.setIcon(Icons.ServerFrame)
        self.drop_target.setObjectName('drop_target')
        self.drop_target.setFixedSize(40, 40)

        # debug
        w1 = ServerWidget(parent=self)
        w1.allow_drag = False
        self.layout_frame.addWidget(w1)

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
