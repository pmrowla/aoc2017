#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 16 module."""
from __future__ import print_function
from string import ascii_lowercase


def spin(l, args):
    n = int(args)
    return l[-n:] + l[:-n]


def _swap(l, a, b):
    l = list(l)
    x = l[a]
    l[a] = l[b]
    l[b] = x
    return l


def exchange(l, args):
    (a, b) = [int(x) for x in args.split('/')]
    return _swap(l, a, b)


def partner(l, args):
    (a, b) = args.split('/')
    return _swap(l, l.index(a), l.index(b))


dance_moves = {
    's': spin,
    'x': exchange,
    'p': partner,
}


def process(puzzle_input):
    permutations = []
    l = list(ascii_lowercase[:16])
    permutations.append(l)
    for step in puzzle_input.split(','):
        l = dance_moves[step[0]](l, step[1:])
    permutations.append(l)
    for i in range(1, 1000000000):
        for step in puzzle_input.split(','):
            l = dance_moves[step[0]](l, step[1:])
        if l in permutations:
            break
        permutations.append(l)
    print(len(permutations))
    p2 = 1000000000 % len(permutations)
    return ''.join(permutations[1]), ''.join(permutations[p2])


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
