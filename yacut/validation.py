import re

from .constants import MAX_LENGHT_SHORT_LINK, REGEX_VALIDATE


def validation_short_link(short_link):
    if len(short_link) > MAX_LENGHT_SHORT_LINK:
        return False
    validated_part_short_link = re.search(REGEX_VALIDATE, short_link)
    return (validated_part_short_link and
            validated_part_short_link.group() == short_link)
