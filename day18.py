#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 18 module."""
from __future__ import print_function

from collections import defaultdict


class CPU(object):

    def __init__(self, prog, prog_id, snd_q, rcv_q):
        self.regs = defaultdict(int)
        self.pc = 0
        self.recovered_freq = None
        self._id = prog_id
        self.regs['p'] = prog_id
        self.prog = prog
        self.snd_q = snd_q
        self.rcv_q = rcv_q
        self.last_freq = 0
        self.snd_count = 0

    def snd(self, args):
        try:
            x = int(args)
        except ValueError:
            x = self.regs[args]
        self.last_freq = x
        # self.snd_q.put(x)
        self.snd_q.append(x)
        self.snd_count += 1
        return 1

    def set(self, args):
        (x, y) = args.split()
        try:
            y = int(y)
        except ValueError:
            y = self.regs[y]
        self.regs[x] = y
        return 1

    def add(self, args):
        (x, y) = args.split()
        try:
            y = int(y)
        except ValueError:
            y = self.regs[y]
        self.regs[x] += y
        return 1

    def mul(self, args):
        (x, y) = args.split()
        try:
            y = int(y)
        except ValueError:
            y = self.regs[y]
        self.regs[x] *= y
        return 1

    def mod(self, args):
        (x, y) = args.split()
        try:
            y = int(y)
        except ValueError:
            y = self.regs[y]
        self.regs[x] %= y
        return 1

    def rcv(self, args):
        try:
            x = int(args)
        except ValueError:
            x = self.regs[args]
        if x != 0 and self.recovered_freq is None:
            self.recovered_freq = self.last_freq
        if self.rcv_q:
            self.regs[args] = self.rcv_q.pop(0)
            return 1
        return 0

    def jgz(self, args):
        (x, y) = args.split()
        try:
            x = int(x)
        except ValueError:
            x = self.regs[x]
        try:
            y = int(y)
        except ValueError:
            y = self.regs[y]
        if x > 0:
            return y
        return 1

    def step(self):
        if self.pc < 0 or self.pc >= len(self.prog):
            return False
        (op, args) = self.prog[self.pc].split(maxsplit=1)
        offset = getattr(self, op)(args)
        self.pc += offset
        if offset:
            return True
        else:
            return False


def process(puzzle_input):
    q_01 = []
    q_10 = []
    p0 = CPU(puzzle_input, 0, q_01, q_10)
    p1 = CPU(puzzle_input, 1, q_10, q_01)
    while p0.step() or p1.step():
        pass
    return p0.recovered_freq, p1.snd_count


def main():
    """Main entry point."""
    import argparse
    import fileinput
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='input file to read ("-" for stdin)')
    args = parser.parse_args()
    try:
        insts = []
        for line in fileinput.input(args.infile):
            line = line.strip()
            if line:
                insts.append(line)
        p1, p2 = process(insts)
        print('Part one: {}'.format(p1))
        print('Part two: {}'.format(p2))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
