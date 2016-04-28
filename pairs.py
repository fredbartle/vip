#!/usr/bin/env python
from __future__ import print_function

import itertools
import sys


SAMPLE_ARRAY = [1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 9]


def pairs(array):
    forward = []
    reverse = []
    results2 = []
    results3 = []

    for a in (1, 2, 3, 4):
        b = 10 - a

        if a in array and b in array:
            # found at least one pair
            a_count = array.count(a)
            b_count = array.count(b)
            forward.extend([(a, b)] * a_count * b_count)
            reverse.extend([(b, a)] * a_count * b_count)

            results2.extend([(a, b), (b, a)])
            results3.append((a, b))

    # 5's are special
    if 5 in array:
        count = array.count(5)
        if count > 1:
            forward.extend([(5, 5)] * count * (count - 1))  # ignore pairing with self

            results2.append((5, 5))
            results3.append((5, 5))

    reverse.reverse()
    results = list(itertools.chain.from_iterable([forward, reverse]))
    results2.sort()
    # results3 are already sorted

    return (results, results2, results3)


def main(array):
    (results1, results2, results3) = pairs(array)

    print('array =', array, '\n')

    print("1) output all pairs (includes duplicates and the reversed ordered pairs):")
    print('>>>', results1, '\n')

    print("2) output unique pairs only once (removes the duplicates but includes the reversed ordered pairs):")
    print('>>>', results2, '\n')

    print("3) output the same combo pair only once (removes the reversed ordered pairs):")
    print('>>>', results3, '\n')


if __name__ == '__main__':
    array = SAMPLE_ARRAY

    if len(sys.argv) > 1:
        array = eval(sys.argv[1])  # this is dangerous without input sanitizing

    main(array)
