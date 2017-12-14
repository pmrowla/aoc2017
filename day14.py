#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 14 module."""
from __future__ import print_function

import day10


def knot_hash(line):
    l = day10.process([ord(x) for x in line.strip()] + [17, 31, 73, 47, 23], rounds=64)
    return day10.knot_hash(l)


def make_grid(puzzle_input):
    grid = []
    for i in range(128):
        line = bin(int.from_bytes(bytes.fromhex(knot_hash('{}-{}'.format(puzzle_input.strip(), i))), byteorder='big')).lstrip('-0b')
        line = '{}{}'.format('0' * (128 - len(line)), line)
        grid.append(list(line))
    return grid


def mark_region(grid, x, y):
    try:
        if x >= 0 and y >= 0 and grid[y][x] == '1':
            grid[y][x] = '0'
            for x2, y2 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                mark_region(grid, x2, y2)
    except IndexError:
        pass


def count_regions(grid):
    regions = 0
    for y in range(128):
        for x in range(128):
            if grid[y][x] == '1':
                regions += 1
                mark_region(grid, x, y)
    return regions


def process(puzzle_input):
    grid = make_grid(puzzle_input)
    return sum([l.count('1') for l in grid]), count_regions(grid)


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
