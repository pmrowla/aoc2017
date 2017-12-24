#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 24 module."""
from __future__ import print_function


def connection(components, port):
    for c in components:
        if c[0] == port:
            yield c, c[1]
        elif c[1] == port:
            yield c, c[0]


def bridges(components, port=0, bridge=[]):
    for c, next_port in connection(components, port):
        new_bridge = list(bridge)
        new_bridge.append(c)
        yield new_bridge
        new_components = list(components)
        new_components.remove(c)
        yield from bridges(new_components, next_port, new_bridge)


def bridge_strength(bridge):
    return sum([sum(x) for x in bridge])


def process(puzzle_input):
    components = [tuple(map(int, line.split('/'))) for line in puzzle_input]
    valid_bridges = list(bridges(components))
    p1 = bridge_strength(sorted(valid_bridges, key=bridge_strength, reverse=True)[0])
    p2 = bridge_strength(sorted(valid_bridges, key=lambda x: (len(x), bridge_strength(x)), reverse=True)[0])
    return p1, p2


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
        p1, p2 = process(puzzle_input)
        print('Part one: {}'.format(p1))
        print('Part two: {}'.format(p2))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
