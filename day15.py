#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 15 module."""
from __future__ import print_function


def generator(initial, factor, mod=None):
    value = initial
    while True:
        value = value * factor % 2147483647
        if mod:
            if value % mod == 0:
                yield value
        else:
            yield value


def process(puzzle_input):
    (init_a, init_b) = [int(x) for x in puzzle_input.split()]
    gen_a = generator(init_a, 16807)
    gen_b = generator(init_b, 48271)
    p1 = 0
    for i in range(40000000):
        a = next(gen_a)
        b = next(gen_b)
        if (a & 0xffff) == (b & 0xffff):
            p1 += 1
    gen_a = generator(init_a, 16807, mod=4)
    gen_b = generator(init_b, 48271, mod=8)
    p2 = 0
    for i in range(5000000):
        a = next(gen_a)
        b = next(gen_b)
        if (a & 0xffff) == (b & 0xffff):
            p2 += 1
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
