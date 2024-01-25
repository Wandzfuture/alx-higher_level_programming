#!/usr/bin/python3
"""Defines a text-indentation function."""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.split("\n")
    for i, line in enumerate(lines):
        lines[i] = line.replace(".", ".  \n").replace("?", "?  \n").replace(":", ":  \n")

    print("\n".join(lines))
