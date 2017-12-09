#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 9 module."""
from __future__ import print_function


def process(puzzle_input):
    open_groups = 0
    in_garbage = False
    cancel_next = False
    scores = []
    garbage_count = 0
    for c in puzzle_input:
        if cancel_next:
            cancel_next = False
        elif in_garbage:
            if c == '!':
                cancel_next = True
            elif c == '>':
                in_garbage = False
            else:
                garbage_count += 1
        else:
            if c == '<':
                in_garbage = True
            elif c == '{':
                open_groups += 1
            elif c == '}':
                scores.append(open_groups)
                open_groups -= 1
    return scores, garbage_count


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
                scores, garbage_count = process(line)
                print('Part one: {}'.format(sum(scores)))
                print('Part two: {}'.format(garbage_count))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
