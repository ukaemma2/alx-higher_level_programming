#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        mykeys = sorted(a_dictionary.keys())
    for k in mykeys:
        print("{:s}: {}".format(k, a_dictionary[k]))
