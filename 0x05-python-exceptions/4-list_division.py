#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []

    for i in range(list_length):

        try:

            if isinstance(my_list_2[i], int) or isinstance(my_list_1, int):

                if my_list_2[i] == 0:

                    new_list.append(0)

                    raise ZeroDivisionError
                else:
                    a = my_list_1[i] / my_list_2[i]
                    new_list.append(a)
            else:
                raise TypeError

        except IndexError:

            new_list.append(0)
            print("out of range")

        except ZeroDivisionError:

            new_list.append(0)
            print("division by 0")
            pass
        except TypeError:
            new_list.append(0)
            print("wrong type")
            pass
        finally:

            pass
    return new_list
