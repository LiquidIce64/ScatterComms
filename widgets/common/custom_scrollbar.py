from PySide6.QtWidgets import QScrollBar, QScrollArea, QWidget
from PySide6.QtCore import Qt


class CustomScrollBar(QScrollBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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


class AnchoredScrollBar(CustomScrollBar):
    def __init__(self, scroll_area: QScrollArea, *args, **kwargs):
        super().__init__(*args, parent=scroll_area, **kwargs)
        self.__scroll_area = scroll_area
        self.__at_bottom = True
        self.__anchor: QWidget | None = None
        self.__anchor_offset = 0
        self.valueChanged.connect(self.update_anchor)
        self.rangeChanged.connect(self.on_range_changed)

    def __page_step(self):
        # Viewport size is more reliable than pageStep as it gets updated first
        if self.orientation() == Qt.Orientation.Vertical:
            return self.__scroll_area.viewport().height()
        else:
            return self.__scroll_area.viewport().width()

    def update_anchor(self):
        self.__at_bottom = self.value() == self.maximum()
        scroll_content = self.__scroll_area.widget()

        # Get widget at the bottom of the visible area
        viewport_bottom = self.value() + self.__page_step()
        widget = scroll_content.childAt(0, viewport_bottom)
        if widget is None:
            # Point is inbetween widgets, search slightly higher
            layout = scroll_content.layout()
            widget = scroll_content.childAt(0, viewport_bottom - layout.spacing() - layout.contentsMargins().bottom())

        # Navigate up the parent tree to make sure widget geometry is relative to scroll content
        while widget is not None and widget.parent() != scroll_content:
            widget = widget.parent()

        self.__anchor = widget
        if widget is not None:
            self.__anchor_offset = viewport_bottom - widget.geometry().bottom()

    def on_range_changed(self, _, maximum):
        if self.__at_bottom:
            self.setValue(maximum)
        elif self.__anchor is not None:
            self.setValue(self.__anchor.geometry().bottom() + self.__anchor_offset - self.__page_step())
        self.update_anchor()
