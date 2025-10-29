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
    if volume_percent == 0:
        return Icons.Media.VolumeMute
    elif volume_percent <= 33:
        return Icons.Media.VolumeLow
    elif volume_percent <= 67:
        return Icons.Media.VolumeMedium
    else:
        return Icons.Media.Volume
