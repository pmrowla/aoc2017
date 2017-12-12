#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 10 module."""
from __future__ import print_function


def walk_conns(conns, prog, prog_set):
    if prog not in prog_set:
        prog_set.add(prog)
        for connected_prog in conns[prog]:
            walk_conns(conns, connected_prog, prog_set)


def process(puzzle_input):
    conns = {}
    for line in puzzle_input:
        line = line.strip()
        if not line:
            continue
        (program, connections) = [x.strip() for x in line.split('<->')]
        conns[program] = [x.strip() for x in connections.split(',')]
    group = set()
    walk_conns(conns, '0', group)
    groups = [group]
    for prog in conns:
        if prog not in [group_set for group_sets in groups for group_set in group_sets]:
            group = set()
            walk_conns(conns, prog, group)
            groups.append(group)
    return len(groups[0]), len(groups)


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
