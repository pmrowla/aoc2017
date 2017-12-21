#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 21 module."""
from __future__ import division, print_function


class Grid(object):

    def __init__(self, grid):
        if isinstance(grid, str):
            self.grid = grid.split('/')
        else:
            self.grid = grid
        if len(self) % 2 != 0 and len(self) % 3 != 0:
            raise ValueError('Invalid grid size: {}'.format(len(self)))

    def __hash__(self):
        return hash(self.transformations())

    def __eq__(self, x):
        return hash(self) == hash(x)

    def match(self, x):
        if hash(self) == hash(x):
            return True
        return False

    def __repr__(self):
        return '<Grid size: {}>'.format(len(self))

    def __str__(self):
        return '/'.join(self.grid)

    def __len__(self):
        if not self.grid:
            return 0
        return len(self.grid)

    def flip_h(self):
        g = list(self.grid)
        g.reverse()
        return Grid(g)

    def flip_v(self):
        return Grid([row[::-1] for row in self.grid])

    def rotate(self, clockwise=True):
        g = []
        if clockwise:
            for i in range(len(self)):
                g.append(''.join([self.grid[j][i] for j in range(len(self) - 1, -1, -1)]))
        else:
            for i in range(len(self) - 1, -1, -1):
                g.append(''.join([self.grid[j][i] for j in range(len(self))]))
        return Grid(g)

    def transformations(self):
        return frozenset([str(g) for g in [self, self.flip_h(), self.flip_v(), self.rotate(), self.rotate(False), self.flip_h().flip_v(), self.rotate().flip_v(), self.rotate(False).flip_v(), self.rotate().flip_h(), self.rotate(False).flip_h(), self.rotate().rotate()]])

    @property
    def on(self):
        return sum([row.count('#') for row in self.grid])

    @property
    def off(self):
        return sum([row.count('.') for row in self.grid])

    def subdivide(self):
        grids = []
        if len(self) % 2 == 0:
            size = 2
        else:
            size = 3
        for i in range(0, len(self), size):
            grid_row = []
            for j in range(0, len(self), size):
                grid_row.append(Grid([self.grid[i + k][j:j + size] for k in range(size)]))
            grids.append(grid_row)
        return grids

    def pprint(self):
        for row in self.grid:
            print(row)

    @classmethod
    def merge(cls, grids):
        if len(grids) == 1:
            return grids[0][0]
        grid = []
        for grid_row in grids:
            for i in range(len(grid_row[0])):
                grid.append(''.join([g.grid[i] for g in grid_row]))
        return Grid(grid)


def _iterate(grid, rules, iterations):
    for i in range(iterations):
        print('--- Iteration {} ---'.format(i))
        new_grid = []
        for row in grid.subdivide():
            new_row = []
            for g in row:
                new_row.append(rules[g])
            new_grid.append(new_row)
        grid = Grid.merge(new_grid)
    return grid


def process(puzzle_input, p1_iterations=5, p2_iterations=18):
    grid = Grid('.#./..#/###')
    rules = {}
    for line in puzzle_input:
        (_in, out) = [x.strip() for x in line.split('=>')]
        rules[Grid(_in)] = Grid(out)
    grid = _iterate(grid, rules, p1_iterations)
    p1 = grid.on
    grid = _iterate(grid, rules, p2_iterations - p1_iterations)
    p2 = grid.on
    return (p1, p2)


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
        (p1, p2) = process(puzzle_input)
        print('Part one: {}'.format(p1))
        print('Part two: {}'.format(p2))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
