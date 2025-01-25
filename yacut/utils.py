from random import choice

from .constants import MAX_LENGHT_URL, ALL_SYMBOLS
from flask import url_for
from .models import URLMap


def get_unique_short_id():
    while True:
        string = ''
        for _ in range(MAX_LENGHT_URL):
            string += choice(ALL_SYMBOLS)
        if not URLMap.query.filter_by(short=string).first():
            return string


def collect_short_link(short):
    return url_for('redirect_a_short_link',
                   short_link=short,
                   _external=True)


def object_short_link(original, short):
    url_map = URLMap(
        original=original,
        short=short
    )
    return url_map
