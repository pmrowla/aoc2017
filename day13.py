#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 13 module."""
from __future__ import print_function


def sum_severity(layers, delay=0):
    return sum([layer * depth for layer, depth in layers if is_caught(layer, depth, delay)])


def is_caught(layer, depth, delay=0):
    return (layer + delay) % (2 * (depth - 1)) == 0


def part_two(layers, delay):
    for layer, depth in layers:
        if is_caught(layer, depth, delay):
            return True
    return False


def process(puzzle_input):
    layers = []
    for line in puzzle_input:
        line = line.strip()
        if not line:
            continue
        (layer, depth) = [int(x.strip()) for x in line.split(':')]
        if depth > 0:
            layers.append((layer, depth))
    delay = 0
    while part_two(layers, delay):
        delay += 1
    return sum_severity(layers), delay


def main():
    """Main entry point."""
    import argparse
    import fileinput

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='input file to read ("-" for stdin)')
    args = parser.parse_args()
    try:
        p1, p2 = process(fileinput.input(args.infile))
        print('Part one: {}'.format(p1))
        print('Part two: {}'.format(p2))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
