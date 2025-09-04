from PySide6.QtWidgets import QWidget, QVBoxLayout


from .server_widget import ServerWidget


class ServerList(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout_widget = QVBoxLayout(self)
        self.layout_widget.setSpacing(6)
        self.layout_widget.setObjectName('layout_widget')
        self.layout_widget.setContentsMargins(0, 0, 0, 0)

        # debug
        self.layout_widget.addWidget(ServerWidget(parent=self))
        w2 = ServerWidget(parent=self)
        w2.selected = True
        w2.update_line()
        self.layout_widget.addWidget(w2)
        w3 = ServerWidget(parent=self)
        w3.notification = True
        w3.update_line()
        self.layout_widget.addWidget(w3)
