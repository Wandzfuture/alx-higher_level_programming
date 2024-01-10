#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_order = list(a_dictionary.keys())
    sort_order.sort()
    for key in sort_order:
        print("{}: {}".format(key, a_dictionary.get(key)))
