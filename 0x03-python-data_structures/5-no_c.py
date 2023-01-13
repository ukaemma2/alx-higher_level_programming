#!/usr/bin/python3

def no_c(my_string):
    new_list = list(my_string)
    new_str = ''
    for i in new_list:
        if i != 'c' and i != 'C':
            new_str += i
    return new_str
