from PySide6.QtWidgets import QScrollBar


class CustomScrollBar(QScrollBar):
    def __init__(self, *args, snap_to_bottom=False, **kwargs):
        super().__init__(*args, **kwargs)
        if snap_to_bottom:
            self.__at_bottom = True
            self.valueChanged.connect(self.on_value_changed)
            self.rangeChanged.connect(self.on_range_changed)
        self.__parent_hovered = False
        self.parent().installEventFilter(self)

    def update_show(self):
        self.setProperty('show', self.__parent_hovered or self.hasFocus())
        self.style().polish(self)

    def focusInEvent(self, event): self.update_show()
    def focusOutEvent(self, event): self.update_show()

    def eventFilter(self, watched, event):
        if event.type() == event.Type.Enter:
            self.__parent_hovered = True
            self.update_show()
        elif event.type() == event.Type.Leave:
            self.__parent_hovered = False
            self.update_show()
        return super().eventFilter(watched, event)

    def on_value_changed(self, value):
        self.__at_bottom = value == self.maximum()

    def on_range_changed(self, _, maximum):
        if self.__at_bottom:
            self.setValue(maximum)
