#!/usr/bin/python3
"""is a function that prints a string in uppercase."""
def uppercase(s):
    result = ""
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        result += c
    print("{}".format(result))
