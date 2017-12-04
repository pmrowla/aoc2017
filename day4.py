#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 4 module."""
from __future__ import print_function

from collections import Counter


def validate_duplicate_words(password):
    words = password.lower().split()
    if len(set(words)) != len(words):
        return False
    return True


def validate_anagrams(password):
    words = list(map(Counter, password.lower().split()))
    for i, word in enumerate(words):
        for j in range(len(words)):
            if i != j and word == words[j]:
                return False
    return True


def part_one(lines):
    count = 0
    for line in lines:
        if validate_duplicate_words(line.strip()):
            count += 1
    return count


def part_two(lines):
    count = 0
    for line in lines:
        if validate_anagrams(line.strip()):
            count += 1
    return count


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
