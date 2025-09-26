from PySide6.QtWidgets import QScrollBar


class SnappingScrollBar(QScrollBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__snap = True
        self.valueChanged.connect(self.on_value_changed)
        self.rangeChanged.connect(self.on_range_changed)

    def on_value_changed(self, value):
        self.__snap = value == self.maximum()

    def on_range_changed(self, _, maximum):
        if self.__snap:
            self.setValue(maximum)
