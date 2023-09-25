#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    b = 0

    for a in range(0, x):

        try:

            print("{:d}".format(my_list[a]), end='')
            b = b + 1

        except ValueError:
            pass
        except TypeError:
            pass

    print("")
    return b
