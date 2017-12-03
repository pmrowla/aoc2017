#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 3 module."""
from __future__ import division, print_function

from itertools import product
from math import ceil, sqrt


def get_grid_size(puzzle_input):
    if puzzle_input < 1:
        raise ValueError('Input must be >= 1')
    elif puzzle_input == 1:
        return 1
    else:
        return ceil(sqrt(puzzle_input))


def get_center(grid_size):
    if grid_size % 2 == 0:
        return grid_size // 2 - 1
    else:
        return grid_size // 2


def get_pos(puzzle_input):
    grid_size = get_grid_size(puzzle_input)
    if puzzle_input == 1:
        extra = 0
    else:
        extra = puzzle_input - pow(grid_size - 1, 2)
    # Origin (0, 0) is in the bottom-left corner
    if grid_size % 2 == 0:
        if extra < grid_size:
            pos = (grid_size - 1, extra - 1)
        else:
            # x = grid_size - (extra - grid_size) - 1
            pos = (2 * grid_size - extra - 1, grid_size - 1)
    else:
        if extra == 0:
            pos = (0, grid_size - 1)
        elif extra < grid_size:
            pos = (0, grid_size - extra)
        else:
            pos = (extra - grid_size, 0)
    return pos


def distance(puzzle_input):
    """Compute the shortest distance from the center to the specified square.

    Args:
        puzzle_input: the input square
    Returns:
        The distance.
    """
    center = get_center(get_grid_size(puzzle_input))
    pos = get_pos(puzzle_input)
    return abs(pos[0] - center) + abs(pos[1] - center)


def init_grid(puzzle_input):
    grid_size = get_grid_size(puzzle_input)
    grid = []
    for i in range(grid_size):
        grid.append([None] * grid_size)
    return grid


def part_one(puzzle_input):
    return distance(puzzle_input)


def sum_adjacent(grid, pos):
    (x, y) = pos
    adjacents = list(product([x - 1, x, x + 1], [y - 1, y, y + 1]))
    adjacents.remove(pos)
    total = 0
    for neighbor in adjacents:
        (x, y) = neighbor
        try:
            if x >= 0 and y >= 0 and grid[y][x] is not None:
                total += grid[y][x]
        except IndexError:
            pass
    return total


def part_two(puzzle_input):
    """Fill puzzle_input number of grid squares.

    Returns:
        First filled square value that is larger than puzzle_input, or None.
    """
    grid_size = get_grid_size(puzzle_input)
    grid = init_grid(puzzle_input)
    x = y = get_center(grid_size)
    grid[y][x] = 1
    i = 1
    x += 1
    current_ring = 2
    while i < puzzle_input:
        grid[y][x] = sum_adjacent(grid, (x, y))
        if grid[y][x] > puzzle_input:
            return grid[y][x]
        # move to the next square along a counter clockwise spiral
        extra = i + 1 - pow(current_ring - 1, 2)
        if current_ring % 2 == 0:
            if extra == 0 or extra >= current_ring:
                # move left
                x -= 1
            else:
                # move up
                y += 1
        else:
            if extra == 0 or extra >= current_ring:
                # move right
                x += 1
            else:
                # move down
                y -= 1
        i += 1
        if i == pow(current_ring, 2):
            current_ring += 1
    return None


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
                puzzle_input = int(line)
                print('Part one: {}'.format(part_one(puzzle_input)))
                print('Part two: {}'.format(part_two(puzzle_input)))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
