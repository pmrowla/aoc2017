#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 25 module."""
from __future__ import print_function

from collections import deque


test_states = {
    'A': {
        0: (1, 1, 'B'),
        1: (0, -1, 'B'),
    },
    'B': {
        0: (1, -1, 'A'),
        1: (1, 1, 'A'),
    },
}


# too lazy to write a parser for this
input_states = {
    'A': {
        0: (1, 1, 'B'),
        1: (0, -1, 'B'),
    },
    'B': {
        0: (1, -1, 'C'),
        1: (0, 1, 'E'),
    },
    'C': {
        0: (1, 1, 'E'),
        1: (0, -1, 'D'),
    },
    'D': {
        0: (1, -1, 'A'),
        1: (1, -1, 'A'),
    },
    'E': {
        0: (0, 1, 'A'),
        1: (0, 1, 'F'),
    },
    'F': {
        0: (1, 1, 'E'),
        1: (1, 1, 'A'),
    },
}


def tape_move(tape, pos):
    if pos == -1:
        tape.appendleft(0)
        pos = 0
    elif pos == len(tape):
        tape.append(0)
    return pos


def process(states=test_states, steps=6):
    tape = deque([0])
    pos = 0
    next_state = 'A'
    for i in range(steps):
        (write, shift, next_state) = states[next_state][tape[pos]]
        tape[pos] = write
        pos = tape_move(tape, pos + shift)
    return sum(tape), None


def main():
    """Main entry point."""
    try:
        p1, p2 = process(states=input_states, steps=12683008)
        print('Part one: {}'.format(p1))
        print('Part two: {}'.format(p2))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
