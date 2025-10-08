import os
from typing import Callable

from PySide6.QtWidgets import QWidget, QFileIconProvider
from PySide6.QtCore import QFileInfo
from PySide6.QtGui import QPixmap, QIcon, QImage

from backend import MessageBackend

registered_extensions: dict[str, tuple[
    Callable[[MessageBackend.Attachment], QWidget],
    Callable[[str], QPixmap | QIcon]
]] = {}


def get_attachment_widget(attachment: MessageBackend.Attachment) -> QWidget:
    ext = os.path.splitext(attachment.filename)[1].lower()
    funcs = registered_extensions.get(ext, None) or registered_extensions['*']
    return funcs[0](attachment)


def get_file_thumbnail(filepath: str) -> QPixmap | QIcon:
    ext = os.path.splitext(filepath)[1].lower()
    funcs = registered_extensions.get(ext, None) or registered_extensions['*']
    return funcs[1](filepath)


def register(*extensions: str):
    def decorator(widget_class):
        def widget_func(attachment: MessageBackend.Attachment):
            return widget_class(attachment)
        register_func(widget_func, widget_class.get_thumbnail, *extensions)
        return widget_class
    return decorator


def register_func(
    widget_func: Callable[[MessageBackend.Attachment], QWidget],
    thumbnail_func: Callable[[str], QPixmap | QIcon],
    *extensions: str
):
    for ext in extensions:
        registered_extensions[ext] = (widget_func, thumbnail_func)


class AttachmentWidget:
    def __init__(self, attachment: MessageBackend.Attachment = None):
        self.attachment = attachment

    def download(self):
        path = self.attachment.filepath
        if path is not None:
            self.on_downloaded(path)
        else:
            # Try to load file from network
            raise NotImplementedError

    @staticmethod
    def get_thumbnail(filepath: str) -> QPixmap | QIcon:
        return QFileIconProvider().icon(QFileInfo(filepath))

    def on_downloaded(self, filepath: str): pass
    def on_load_failed(self): pass
