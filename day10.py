#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 10 module."""
from __future__ import print_function


def process(lengths, list_size=256, rounds=1):
    l = list(range(list_size))
    i = 0
    skip_size = 0
    for r in range(rounds):
        for length in lengths:
            start = i
            end = (i + length - 1) % list_size
            for j in range(length // 2):
                tmp = l[start]
                l[start] = l[end]
                l[end] = tmp
                end -= 1
                start = (start + 1) % list_size
            i = (i + length + skip_size) % list_size
            skip_size += 1
    return l


def knot_hash(l):
    dense_hash = []
    n = 0
    for i in range(len(l)):
        if i % 16 == 0:
            if i > 0:
                dense_hash.append(n)
            n = l[i]
        else:
            n ^= l[i]
    dense_hash.append(n)
    return ''.join(['{:02x}'.format(x) for x in dense_hash])


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
            lengths = [int(x.strip()) for x in line.split(',')]
            l = process(lengths)
            print('Part one: {}'.format(l[0] * l[1]))
            lengths = [ord(x) for x in line] + [17, 31, 73, 47, 23]
            l = process(lengths, rounds=64)
            print('Part two: {}'.format(knot_hash(l)))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
