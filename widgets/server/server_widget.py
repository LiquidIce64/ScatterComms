from PySide6.QtWidgets import QWidget

from .ui_server_widget import Ui_widget_server


class ServerWidget(QWidget, Ui_widget_server):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.icon.painter_mask = self.icon.RoundedRectMask()

        self.btn.focused.connect(self.update_line)
        self.btn.focusLost.connect(self.update_line)

        self.selected = False
        self.notification = False

        self.update_line()

    def update_line(self):
        if self.selected:
            self.line.setFixedHeight(self.height())
            self.line.setVisible(True)
        elif self.underMouse() or self.hasFocus():
            self.line.setFixedHeight(self.height() // 2)
            self.line.setVisible(True)
        elif self.notification:
            self.line.setFixedHeight(4)
            self.line.setVisible(True)
        else:
            self.line.setVisible(False)

    def enterEvent(self, event):
        self.update_line()

    def leaveEvent(self, event):
        self.update_line()
