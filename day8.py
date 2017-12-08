#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 8 module."""
from __future__ import print_function

import re
from collections import defaultdict


def test_cond(registers, cond, cond_reg, cond_val):
    conds = {
        '>': lambda x, y: x > y,
        '>=': lambda x, y: x >= y,
        '<': lambda x, y: x < y,
        '<=': lambda x, y: x <= y,
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y,
    }
    return conds[cond](registers[cond_reg], cond_val)


def do_op(registers, op, reg, val):
    ops = {
        'inc': lambda x, y: x + y,
        'dec': lambda x, y: x - y,
    }
    return ops[op](registers[reg], val)


def cpu(instructions):
    registers = defaultdict(int)
    max_val = 0
    for inst in instructions:
        pattern = r'^(?P<reg>\w+) (?P<op>\w+) (?P<val>[\-0-9]+) if (?P<cond_reg>\w+) (?P<cond>[<>=!]+) (?P<cond_val>[\-0-9]+)$'
        m = re.match(pattern, inst)
        if m:
            reg = m.group('reg')
            op = m.group('op')
            val = int(m.group('val'))
            cond_reg = m.group('cond_reg')
            cond = m.group('cond')
            cond_val = int(m.group('cond_val'))
            if test_cond(registers, cond, cond_reg, cond_val):
                registers[reg] = do_op(registers, op, reg, val)
        max_val = max(list(registers.values()) + [max_val])
    return (registers, max_val)


def main():
    """Main entry point."""
    import argparse
    import fileinput

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='input file to read ("-" for stdin)')
    args = parser.parse_args()
    try:
        instructions = []
        for line in fileinput.input(args.infile):
            line = line.strip()
            if line:
                instructions.append(line)
        (registers, max_val) = cpu(instructions)
        print('Part one: {}'.format(max(registers.values())))
        print('Part two: {}'.format(max_val))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
