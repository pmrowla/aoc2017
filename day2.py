#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 1 module."""
from __future__ import division, print_function


def diff(row):
    row = sorted(map(int, row))
    return row[-1] - row[0]


def div(row):
    row = sorted(map(int, row), reverse=True)
    for i, n in enumerate(row):
        for m in row[i + 1:]:
            if (n % m) == 0:
                return n // m
    return 0


def checksum(sheet, row_func=diff):
    """Compute the checksum of a spreadsheet.

    Args:
        sheet (iterable): iterable of iterables
        row_func (callable): function to be called for each row. The result
            will be added to the checksum.

    Returns:
        The sum of row_func for each row in sheet.
    """
    return sum(map(row_func, sheet))


def part_one(sheet):
    return checksum(sheet)


def part_two(sheet):
    return checksum(sheet, row_func=div)


def main():
    """Main entry point."""
    import argparse
    import fileinput

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='input file to read ("-" for stdin)')
    args = parser.parse_args()
    try:
        puzzle_input = []
        for line in fileinput.input(args.infile):
            puzzle_input.append(line.strip().split())
    except KeyboardInterrupt:
        pass
    print('Part one: {}'.format(part_one(puzzle_input)))
    print('Part two: {}'.format(part_two(puzzle_input)))


if __name__ == '__main__':
    main()
