#!/usr/bin/python3
"""Reads from standard input and computes metrics."""
if __name__ == "__main__":
import sys
from collections import defaultdict

def print_metrics(total_size, status_counts):
    """Prints the total file size and the count of each status code.

    Args:
        total_size: The total file size.
        status_counts: A dictionary containing status code counts.

    Returns:
        None
    """
    print(f"File size: {total_size}")
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")

def main():
    """Reads stdin line by line and computes metrics."""
    total_size = 0
    status_counts = defaultdict(int)
    try:
        for idx, line in enumerate(sys.stdin, start=1):
            _, _, _, status_code_str, size_str = line.strip().rsplit(' ', 4)
            status_code = int(status_code_str)
            size = int(size_str)
            total_size += size
            status_counts[status_code] += 1
            if idx % 10 == 0:
                print_metrics(total_size, status_counts)
    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
