#!/usr/bin/python3
import sys


def magic_calculation(a, b):
    result = 0

    try:
        for i in range(1, 3):
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i

        result += a + b
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        result = None

    return (result)
