#!/usr/bin/python3

def element_at(my_list, idx):
    
    n = len(my_list)

    if idx > n or idx < 0:

        return None

    elif idx == n:


        return my_list[n - 1]
    else:
        return my_list[idx]
