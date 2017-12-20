#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 20 module."""
from __future__ import print_function
import re


class Particle(object):

    def __init__(self, _id, s):
        self._id = _id
        m = re.match(r'^p=<(?P<position>.*)>, v=<(?P<velocity>.*)>, a=<(?P<acceleration>.*)>$', s.strip())
        if not m:
            raise ValueError
        for attr in ['position', 'velocity', 'acceleration']:
            setattr(self, attr, [int(x) for x in m.group(attr).strip().split(',')])

    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return '{}: p={}, v={}, a={}'.format(self._id, self.position, self.velocity, self.acceleration)

    def __repr__(self):
        return 'Particle<{}>'.format(str(self))

    def update(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.velocity[2] += self.acceleration[2]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

    @property
    def distance(self):
        return sum([abs(x) for x in self.position])


def process(puzzle_input, check_collisions=False):
    particles = [Particle(i, line) for i, line in enumerate(puzzle_input)]
    while True:
        if check_collisions:
            collisions = set()
            for i, p1 in enumerate(particles):
                for p2 in particles[i + 1:]:
                    if p1.position == p2.position:
                        collisions.add(p1)
                        collisions.add(p2)
            for p in collisions:
                particles.remove(p)
        [p.update() for p in particles]
        new = sorted(particles, key=lambda p: p.distance)
        if new == particles:
            break
        particles = new
    return particles


def part_one(puzzle_input):
    return process(puzzle_input)[0]._id


def part_two(puzzle_input):
    return len(process(puzzle_input, check_collisions=True))


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
            puzzle_input.append(line)
        print('Part one: {}'.format(part_one(puzzle_input)))
        print('Part two: {}'.format(part_two(puzzle_input)))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
