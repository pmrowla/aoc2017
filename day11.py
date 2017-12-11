#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 10 module."""
from __future__ import print_function


merge = {
    'n': {
        'se': ['ne'],
        's': [],
        'sw': ['nw'],
    },
    'ne': {
        's': ['se'],
        'sw': [],
        'nw': ['n'],
    },
    'se': {
        'sw': ['s'],
        'nw': [],
        'n': 'ne',
    },
}


def compress_one(steps):
    if len(steps) <= 1:
        return False
    for d1 in merge:
        if d1 in steps:
            for d2 in merge[d1]:
                if d2 in steps:
                    steps.remove(d1)
                    steps.remove(d2)
                    steps.extend(merge[d1][d2])
                    return True
    return False


def process(steps):
    max_distance = 0
    steps = list(steps)
    compressed = []
    for i in steps:
        compressed.append(i)
        while compress_one(compressed):
            pass
        max_distance = max(max_distance, len(compressed))
    return len(compressed), max_distance


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
                steps = [step.strip() for step in line.split(',')]
                p1, p2 = process(steps)
                print('Part one: {}'.format(p1))
                print('Part two: {}'.format(p2))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
