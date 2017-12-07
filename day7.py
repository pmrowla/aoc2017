#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Advent of Code 2017 day 7 module."""
from __future__ import print_function

from collections import Counter
import re


def build_tree(puzzle_input):
    tree = {}
    weights = {}
    for line in puzzle_input:
        line = line.strip()
        pattern = r'^(?P<name>\w+)\s+\((?P<weight>\d+)\)( -> (?P<children>.*))?$'
        m = re.match(pattern, line)
        if m:
            d = m.groupdict()
            name = d.get('name')
            weight = int(d.get('weight'))
            children = d.get('children')
            weights[name] = weight
            if children:
                tree[name] = [x.rstrip(',') for x in children.split()]
    root = get_root(tree, weights)
    return root, tree, weights


def get_root(tree, weights):
    for name in weights:
        has_parent = False
        for parent in tree:
            if name in tree[parent]:
                has_parent = True
                break
        if not has_parent:
            return name


def sum_stack(root, tree, weights):
    total = weights[root]
    for child in tree.get(root, []):
        total += sum_stack(child, tree, weights)
    return total


def is_balanced(root, tree, weights):
    stacks = []
    for child in tree.get(root, []):
        stacks.append(sum_stack(child, tree, weights))
    return stacks[1:] == stacks[:-1]


def get_unbalanced(root, tree, weights):
    if root in tree:
        for child in tree[root]:
            if not is_balanced(child, tree, weights):
                return get_unbalanced(child, tree, weights)
    return root


def part_two(root, tree, weights):
    unbalanced = get_unbalanced(root, tree, weights)
    sums = [(child, sum_stack(child, tree, weights)) for child in tree[unbalanced]]
    c = Counter([x[1] for x in sums])
    old_weight = 0
    for child, stack in sums:
        if c[stack] == 1:
            old_weight = weights[child]
            old_sum = stack
        else:
            new_sum = stack
    return old_weight + new_sum - old_sum


def main():
    """Main entry point."""
    import argparse
    import fileinput

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='input file to read ("-" for stdin)')
    args = parser.parse_args()
    try:
        (root, tree, weights) = build_tree(fileinput.input(args.infile))
        print('Part one: {}'.format(root))
        print('Part two: {}'.format(part_two(root, tree, weights)))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
