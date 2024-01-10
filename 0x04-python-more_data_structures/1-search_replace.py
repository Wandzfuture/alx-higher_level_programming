#!/usr/bin/python3
#1-search_replace.py

def search_replace(my_list, search, replace):
    def find_search(element):
        return element if element != search else replace
    return list(map(find, my_list))
