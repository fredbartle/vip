#!/usr/bin/env python
from __future__ import print_function


SAMPLE_ARRAY = [1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 9]


def pairs(array):
    results = []

    for a in (1, 2, 3, 4):
        b = 10 - a

        if a in array and b in array:
            # found at least one pair
            a_count = array.count(a)
            b_count = array.count(b)
            results.extend([(a, b)] * a_count * b_count)  # forward
            results.extend([(b, a)] * a_count * b_count)  # reverse

    # 5's are special, ignore pairing with self
    if 5 in array:
        count = array.count(5)
        results.extend([(5, 5)] * count * (count - 1))

    results1 = sorted(results)
    results2 = sorted(set(results1))  # remove duplicates
    results3 = sorted(set([tuple(t) for t in map(sorted, results2)]))  # remove reversed

    return (results1, results2, results3)


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
    main(SAMPLE_ARRAY)
