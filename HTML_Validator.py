

import re


def validate_html(html):
    '''
    This function performs a limited version of html validation by
    checking whether every opening tag has a corresponding closing tag.
    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    if len(html) == 0:
        return True
    tag = _extract_tags(html)
    if not tag:
        return False
    s = []
    index = 0
    balanced = True
    while index < len(tag) and balanced:
        a = tag[index]
        b = a[1:-1]
        if "/" not in a:
            s.append(b)
        else:
            if len(s) == 0:
                balanced = False
            else:
                top = s.pop()
                if not top == b[1:]:
                    balanced = False
        index += 1
    if balanced and len(s) == 0:
        return True
    else:
        return False


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be
    used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the
    input string,stripping out all text not contained within angle
    brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = re.findall(r'<[^>]+>', html)
    return tags
