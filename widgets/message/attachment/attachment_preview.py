from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Qt, QSize

from .attachment_widget import get_file_thumbnail
from widgets.common import IconButton, MaskedImage
from resources import Icons


class AttachmentPreview(QFrame):
    def __init__(self, filepath: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filepath = filepath
        self.setObjectName('attachment_preview')
        self.setFixedSize(64, 64)
        self.setStyleSheet(
            '#attachment_preview {border: 1px solid #808080; border-radius: 8px;}'
            '#btn_remove {background-color: #808080; border: none; border-radius: 8px;}'
            '#btn_remove:hover {background-color: red;}'
        )
        self.icon_preview = MaskedImage(parent=self)
        self.icon_preview.setObjectName('icon_preview')
        self.icon_preview.setGeometry(0, 0, 64, 64)
        self.icon_preview.painter_mask = self.icon_preview.RoundedRectMask(8)
        self.icon_preview.setPixmap(get_file_thumbnail(filepath))
        self.remove_btn = IconButton(parent=self)
        self.remove_btn.setObjectName('btn_remove')
        self.remove_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.remove_btn.setGeometry(48, 0, 16, 16)
        self.remove_btn.setIconSize(QSize(8, 8))
        self.remove_btn.setIcon(Icons.Cross)
        self.remove_btn.clicked.connect(self.deleteLater)
