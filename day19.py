#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 19 module."""
from __future__ import print_function


class Route(object):

    MOVES = {
        'u': lambda x, y: (x, y - 1),
        'd': lambda x, y: (x, y + 1),
        'l': lambda x, y: (x - 1, y),
        'r': lambda x, y: (x + 1, y),
    }

    def __init__(self, grid):
        self.grid = grid
        self.x, self.y = self._find_start()
        self.direction = 'd'
        self._path = []
        self.steps = 0

    @property
    def pos(self):
        return self.x, self.y

    def _find_start(self):
        return self.grid[0].index('|'), 0

    def _turn(self):
        if self.direction in 'ud':
            to_check = 'lr'
        else:
            to_check = 'ud'
        for d in to_check:
            x, y = self.MOVES[d](self.x, self.y)
            try:
                if x >= 0 and y >= 0 and not self.grid[y][x].isspace():
                    return d
            except IndexError:
                pass
        return None

    def _trace(self):
        try:
            c = self.grid[self.y][self.x]
        except IndexError:
            return None
        if self.y < 0 or self.x < 0 or c.isspace():
            return None
        elif c == '+':
            self.direction = self._turn()
            if not self.direction:
                return None
        elif c not in '-|':
            self._path.append(c)
        self.x, self.y = self.MOVES[self.direction](self.x, self.y)
        self.steps += 1
        return self.pos

    def path(self):
        if not self._path:
            while self._trace():
                pass
        return ''.join(self._path)


def process(puzzle_input):
    r = Route(puzzle_input)
    return r.path(), r.steps


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
        p1, p2 = process(puzzle_input)
        print('Part one: {}'.format(p1))
        print('Part two: {}'.format(p2))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
