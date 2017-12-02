#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 1 module."""
from __future__ import division, print_function


def sum_digits(digits, cmp_index=lambda x: x + 1):
    """Sum all digits that match the another digit in the list.

    Args:
        digits (iterable): Input digit list.
        cmp_index (callable, optional): Function to be used when determining
            index of the digit to compare to the current digit. Defaults to
            the next digit (j = i + 1).

    Returns:
        The sum of all digits that match the digit at index cmp_index().
    """
    total = 0
    digits = list(map(int, digits))
    for i in range(len(digits)):
        j = cmp_index(i) % len(digits)
        if digits[i] == digits[j]:
            total += digits[i]
    return total


def part_one(digits):
    return sum_digits(digits)


def part_two(digits):
    if len(digits) % 2 != 0:
        raise(TypeError('list must contain an even number of digits'))
    return sum_digits(digits, lambda x: x + len(digits) // 2)


def main():
    """Main entry point."""
    import argparse
    import fileinput

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='input file to read ("-" for stdin)')
    args = parser.parse_args()
    try:
        for line in fileinput.input(args.infile):
            puzzle_input = line.strip()
            print('Part one: {}'.format(part_one(puzzle_input)))
            print('Part two: {}'.format(part_two(puzzle_input)))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
