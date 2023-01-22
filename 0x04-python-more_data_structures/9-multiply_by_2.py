#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new_dict = dict(a_dictionary)
        for i, v in new_dict.items():
            new_dict[i] = v * 2
        return new_dict
