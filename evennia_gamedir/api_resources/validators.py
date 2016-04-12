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
        markdown.markdown(value, output_format='html5'),
        tags=ALLOWED_TAGS,
    )
    return retval
