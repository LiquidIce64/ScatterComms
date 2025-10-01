from PySide6.QtWidgets import QFrame

from .attachment_widget import AttachmentWidget, register
from backend.attachment import AttachmentBackend


@register('*')
class GenericFileWidget(QFrame, AttachmentWidget):
    def __init__(self, attachment: AttachmentBackend.Attachment):
        super().__init__(attachment=attachment)
        self.load_file()
