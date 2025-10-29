import math

from PySide6.QtWidgets import QApplication

from resources import Icons


def ms_to_timestamp(milliseconds: int) -> str:
    """
    Converts time in milliseconds to a timestamp string
    :param milliseconds: time in milliseconds
    :return: string timestamp formatted as [hh:]mm:ss
    """
    seconds = milliseconds // 1000
    minutes = seconds // 60
    seconds %= 60
    if minutes < 60:
        return f'{minutes}:{seconds:02d}'
    hours = minutes // 60
    minutes %= 60
    return f'{hours}:{minutes:02d}:{seconds:02d}'


def get_volume_icon(volume_percent: int):
    """
    Maps volume percentage to a corresponding volume icon
    :param volume_percent: volume percentage
    :return: volume icon
    """
    if volume_percent == 0:
        return Icons.Media.VolumeMute
    elif volume_percent <= 33:
        return Icons.Media.VolumeLow
    elif volume_percent <= 67:
        return Icons.Media.VolumeMedium
    else:
        return Icons.Media.Volume


def format_file_size(size: int):
    """
    Converts file size to a readable format
    :param size: file size in bytes
    :return: string in readable format (e.g. 1 KB)
    """
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    unit_ind = min(
        int(math.log(size, 1024)),
        len(units)-1
    ) if size > 0 else 0
    value = size / (1024 ** unit_ind)
    unit = QApplication.translate('file_size', units[unit_ind])
    return f'{value:.{0 if unit_ind == 0 else 1}f}\xa0{unit}'
