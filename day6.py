#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 4 module."""
from __future__ import print_function


def redistribute(banks):
    seen = []
    count = 0
    while tuple(banks) not in seen:
        seen.append(tuple(banks))
        i = banks.index(max(banks))
        redist = banks[i]
        banks[i] = 0
        while redist > 0:
            i += 1
            if i == len(banks):
                i = 0
            banks[i] += 1
            redist -= 1
        count += 1
    return (count, count - seen.index(tuple(banks)))


def main():
    """Main entry point."""
    import argparse
    import fileinput

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='input file to read ("-" for stdin)')
    args = parser.parse_args()
    try:
        for line in fileinput.input(args.infile):
            line = line.strip()
            if line:
                puzzle_input = list(map(int, line.split()))
                (part_one, part_two) = redistribute(puzzle_input)
                print('Part one: {}'.format(part_one))
                print('Part two: {}'.format(part_two))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
