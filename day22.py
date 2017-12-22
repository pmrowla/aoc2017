#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 22 module."""
from __future__ import print_function


DIRS = ('n', 'e', 's', 'w')


MOVES = {
    'n': lambda x, y: (x, y + 1),
    'e': lambda x, y: (x + 1, y),
    's': lambda x, y: (x, y - 1),
    'w': lambda x, y: (x - 1, y)
}


def init_infected(puzzle_input):
    infected = set()
    center = len(puzzle_input) // 2
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input)):
            if puzzle_input[i][j] == '#':
                infected.add((j - center, center - i))
    return infected


def part_one(puzzle_input):
    infected = init_infected(puzzle_input)
    _dir = 0
    x, y = (0, 0)
    infections = 0
    for i in range(10000):
        if (x, y) in infected:
            _dir = (_dir + 1) % len(DIRS)
            infected.remove((x, y))
        else:
            _dir = (_dir - 1) % len(DIRS)
            infected.add((x, y))
            infections += 1
        x, y = MOVES[DIRS[_dir]](x, y)
    return infections


def part_two(puzzle_input):
    infected = init_infected(puzzle_input)
    weakened = set()
    flagged = set()
    _dir = 0
    x, y = (0, 0)
    infections = 0
    for i in range(10000000):
        if (x, y) in infected:
            _dir = (_dir + 1) % len(DIRS)
            infected.remove((x, y))
            flagged.add((x, y))
        elif (x, y) in weakened:
            weakened.remove((x, y))
            infected.add((x, y))
            infections += 1
        elif (x, y) in flagged:
            _dir = (_dir + 2) % len(DIRS)
            flagged.remove((x, y))
        else:
            _dir = (_dir - 1) % len(DIRS)
            weakened.add((x, y))
        x, y = MOVES[DIRS[_dir]](x, y)
    return infections


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
            puzzle_input.append(line)
        print('Part one: {}'.format(part_one(puzzle_input)))
        print('Part two: {}'.format(part_two(puzzle_input)))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
