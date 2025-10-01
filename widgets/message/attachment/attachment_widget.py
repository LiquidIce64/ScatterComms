import os
from typing import Callable
from PySide6.QtWidgets import QWidget

from backend.attachment import AttachmentBackend

registered_extensions: dict[str, Callable[[AttachmentBackend.Attachment], QWidget]] = {}


def get_attachment_widget(attachment: AttachmentBackend.Attachment) -> QWidget:
    ext = os.path.splitext(attachment.filename)[1].lower()
    func = registered_extensions.get(ext, None) or registered_extensions['*']
    return func(attachment)


def register(*extensions: str):
    def decorator(widget_class: type):
        def func(attachment: AttachmentBackend.Attachment):
            return widget_class(attachment)
        for ext in extensions:
            registered_extensions[ext] = func
        return widget_class
    return decorator


class AttachmentWidget:
    def __init__(self, attachment: AttachmentBackend.Attachment):
        self.attachment = attachment

    def load_file(self):
        path = self.attachment.filepath
        if path is not None:
            self.on_load(path)
        else:
            # Try to load file from network
            raise NotImplementedError

    def on_load(self, filepath: str): pass
    def on_load_failed(self): pass
