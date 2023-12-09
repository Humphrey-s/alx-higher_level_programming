#!/usr/bin/python3
"""definition of say_my_name"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>"""

    if isinstance(first_name, str) and isinstance(last_name, str):

        if len(first_name) == 0 and len(last_name) == 0:
            pass
        print("My name is {} {}".format(first_name, last_name))

    elif not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        pass
