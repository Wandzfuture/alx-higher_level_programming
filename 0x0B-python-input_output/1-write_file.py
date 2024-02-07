#!/usr/bin/python3
"""Defines a file-writing function.
"""

def write_file(filename="", text=""):
    """Write a string to a text file (UTF8)

       return the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text).
