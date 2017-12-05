#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 4 module."""
from __future__ import print_function


def count_steps(offsets, func=lambda x: x + 1):
    steps = 0
    i = 0
    while i < len(offsets):
        j = i + offsets[i]
        offsets[i] = func(offsets[i])
        i = j
        steps += 1
    return steps


def func_2(x):
    if x >= 3:
        return x - 1
    else:
        return x + 1


def part_one(puzzle_input):
    return count_steps(puzzle_input)


def part_two(puzzle_input):
    return count_steps(puzzle_input, func=func_2)


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
            line = line.strip()
            if line:
                puzzle_input.append(line)
        puzzle_input = list(map(int, puzzle_input))
        print('Part one: {}'.format(part_one(list(puzzle_input))))
        print('Part two: {}'.format(part_two(list(puzzle_input))))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
