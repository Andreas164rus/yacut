from .constants import ALL_SYMBOLS


def validation_short_link(short_link):
    if len(short_link) > 16:
        return False
    for symbol in short_link:
        if symbol not in ALL_SYMBOLS:
            return False
    return True