
# !/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking
    whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    tag_front = []
    tag_list = _extract_tags(html)
    if tag_list == []:
        return False
    valid = True
    for i in range(len(tag_list)):
        tag = tag_list[i]
        if "/" not in tag:
            tag_front.append(tag)
        else:
            if tag_front == []:
                valid = False
            else:
                if tag_front[-1] == tag:
                    tag_front.pop()
                else:
                    return False
    return valid and tag_front == []
    # HINT:
    # use the _extract_tags function below to generate
    # a list of html tags without any extra text;
    # then process these html tags using the balanced
    # parentheses algorithm from the class/book
    # the main difference between your code and the code from class will
    # be that you will have to keep track of
    # not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions
    that are not meant
    to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags
    contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tag_list = []
    for i in range(len(html)):
        if html[i] == "<":
            for j in range(i, len(html)):
                if html[j] == ">":
                    tag_list.append(html[i:j + 1])
                    break
    return tag_list
