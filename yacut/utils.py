from random import choice

from .constants import MAX_LENGHT_URL, ALL_SYMBOLS
from flask import url_for
from .models import URLMap


def get_random_string(lenght=MAX_LENGHT_URL):
    string = ''
    for _ in range(lenght):
        string += choice(ALL_SYMBOLS)
    return string


def collect_short_link(short):
    return url_for('redirect_a_short_link',
                   short_link=short,
                   _external=True)


def object_short_link(original, short=None):
    if short is None:
        new_short = False
        while not new_short:
            short = get_random_string()
            if URLMap.query.filter_by(short=short).first():
                continue
            new_short = True
    url_map = URLMap(
        original=original,
        short=short
    )
    return url_map


def short_link_in_db_exists(short_link):
    return (
        short_link and
        URLMap.query.filter_by(short=short_link).first() is not None
    )