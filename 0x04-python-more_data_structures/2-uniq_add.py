#!/usr/bin/python3


def uniq_add(my_list=[]):
    """adds all unique integers in a list"""
    uniq_list = set(my_list)
    number = 0

    for i in uniq_list:
        number += i

    return (number)
