from .attachment_widget import AttachmentWidget, register
from widgets.common import AudioPlayer
from backend import MessageBackend


@register(
    '.mp3', '.m4a', '.mp4a',
    '.wav', '.wave',
    '.ogg', '.oga',
    '.aac', '.adts',
    '.wma', '.avi', '.flac',
)
class AudioWidget(AudioPlayer, AttachmentWidget):
    def __init__(self, attachment: MessageBackend.Attachment = None):
        super().__init__()
        self.attachment = attachment
        self.setObjectName('video_widget')
        self.setFixedWidth(350)
        self.btn_file.setText(self.attachment.filename)
        self.setEnabled(False)
        self.download()

    def on_downloaded(self, filepath: str):
        self.set_source(filepath)
        self.setEnabled(True)
