from copy import copy

import bleach
import markdown

ALLOWED_TAGS = copy(bleach.ALLOWED_TAGS)
ALLOWED_TAGS += ['p', 'br', 'pre']


def markdown_str(value):
    """
    Runs the value through a markdown to HTML conversion process.

    :param str value:
    :rtype: str
    :return: The rendered HTML for the markdown.
    """
    retval = bleach.clean(
        markdown.markdown(value, output_format='html'),
        tags=ALLOWED_TAGS,
    )
    return retval


def game_short_description(value, name):
    max_len = 255
    if len(value) > max_len:
        raise ValueError(
            "Your {} can not exceed {} characters.".format(
                name, max_len))
    return value
