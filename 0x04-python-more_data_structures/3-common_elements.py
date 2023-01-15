#!/usr/bin/python3

def common_elements(set_1, set_2):
    if set_1 is not None and set_2 is not None:

        set_new_1 = set(set_1)
        set_new_2 = set(set_2)

        if (set_new_1 & set_new_2):
            total = set_new_1 & set_new_2
        return total
