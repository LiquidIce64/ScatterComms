import os
from typing import Callable, cast

from PySide6.QtWidgets import QWidget, QFileIconProvider, QFileDialog, QApplication
from PySide6.QtCore import QFileInfo, QStandardPaths, QFile, QTemporaryDir, QMimeData, QUrl
from PySide6.QtGui import QPixmap, QIcon

from resources import Icons
from widgets.common import MenuWidget
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

    def context_menu_buttons(self, menu: MenuWidget):
        if self.attachment.filepath is None:
            return
        menu.add_button('Save attachment', Icons.Generic.Save, 4, slot=self.save_attachment)
        menu.add_button('Copy attachment', Icons.Generic.Copy, 4, slot=self.copy_attachment)

    def save_attachment(self):
        downloads_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DownloadLocation)
        new_filepath = QFileDialog.getSaveFileName(
            parent=cast(QWidget, self),
            caption=QApplication.translate('file_dialog', 'Save file'),
            dir=f'{downloads_dir}/{self.attachment.filename}'
        )[0]
        if new_filepath:
            QFile.copy(self.attachment.filepath, new_filepath)

    def copy_attachment(self):
        temp_dir = QTemporaryDir()
        temp_dir.setAutoRemove(False)
        if not temp_dir.isValid():
            raise RuntimeError(temp_dir.errorString())
        new_filepath = temp_dir.filePath(self.attachment.filename)
        QFile.copy(self.attachment.filepath, new_filepath)

        file_url = QUrl.fromLocalFile(new_filepath)
        mime_data = QMimeData()
        mime_data.setUrls([file_url])
        QApplication.clipboard().setMimeData(mime_data)

    @staticmethod
    def get_thumbnail(filepath: str) -> QPixmap | QIcon:
        return QFileIconProvider().icon(QFileInfo(filepath))

    def on_downloaded(self, filepath: str): pass
    def on_load_failed(self): pass
