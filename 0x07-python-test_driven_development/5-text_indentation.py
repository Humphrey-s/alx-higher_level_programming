#!/usr/bin/python3
"""def text_indentation"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str) or text is None:
        raise TypeError("text must be a string")

    a = 0
    for i in text:

        if a == 0 and i == " ":
            continue

        print(i, end='')
        a = 9

        if i == '.' or i == '?' or i == ':':
            print("\n")
