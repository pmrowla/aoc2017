#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 18 module."""
from __future__ import print_function

from collections import defaultdict


class CPU(object):

    def __init__(self, prog, debug=True):
        self.regs = defaultdict(int)
        self.pc = 0
        self.prog = prog
        self.inst_counter = defaultdict(int)
        if not debug:
            self.regs['a'] = 1

    def set(self, args):
        (x, y) = args.split()
        try:
            y = int(y)
        except ValueError:
            y = self.regs[y]
        self.regs[x] = y
        return 1

    def sub(self, args):
        (x, y) = args.split()
        try:
            y = int(y)
        except ValueError:
            y = self.regs[y]
        self.regs[x] -= y
        return 1

    def mul(self, args):
        (x, y) = args.split()
        try:
            y = int(y)
        except ValueError:
            y = self.regs[y]
        self.regs[x] *= y
        return 1

    def jnz(self, args):
        (x, y) = args.split()
        try:
            x = int(x)
        except ValueError:
            x = self.regs[x]
        try:
            y = int(y)
        except ValueError:
            y = self.regs[y]
        if x != 0:
            return y
        return 1

    def step(self):
        if self.pc < 0 or self.pc >= len(self.prog):
            return False
        (op, args) = self.prog[self.pc].split(maxsplit=1)
        offset = getattr(self, op)(args)
        self.pc += offset
        self.inst_counter[op] += 1
        if offset:
            return True
        else:
            return False


def part_one(puzzle_input):
    p = CPU(puzzle_input)
    while p.step():
        pass
    return p.inst_counter['mul']


def part_two(puzzle_input):
    # this is the decompiled version of what the program does (it just checks
    # for primes between b and c). depending on your input the required range()
    # might be different
    h = 0
    for b in range(108400, 125401, 17):
        for d in range(2, b):
            if b % d == 0:
                h += 1
                break
    return h


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
        print('Part one: {}'.format(part_one(puzzle_input)))
        print('Part two: {}'.format(part_two(puzzle_input)))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
