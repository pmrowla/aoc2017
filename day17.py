#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 17 module."""
from __future__ import print_function


def spinlock(step):
    buf = [0]
    pos = 0
    i = 0
    while True:
        i += 1
        pos = ((pos + step) % len(buf)) + 1
        buf.insert(pos, i)
        yield (buf, pos)


def spinlock2(step):
    pos = 0
    i = 0
    while True:
        i += 1
        pos = ((pos + step) % i) + 1
        yield pos


def process(puzzle_input):
    s = spinlock(int(puzzle_input))
    for i in range(1, 2018):
        (buf, pos) = next(s)
    p1 = buf[pos + 1]
    s = spinlock2(int(puzzle_input))
    p2 = 0
    for i in range(1, 50000000):
        pos = next(s)
        if pos == 1:
            p2 = i
    return p1, p2


def main():
    """Main entry point."""
    import argparse
    import fileinput
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='input file to read ("-" for stdin)')
    args = parser.parse_args()
    try:
        for line in fileinput.input(args.infile):
            p1, p2 = process(line.strip())
            print('Part one: {}'.format(p1))
            print('Part two: {}'.format(p2))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
