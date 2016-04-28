from unittest import TestCase

from pairs import pairs


class PairsTest(TestCase):

    def test_sample_array(self):
        ARRAY = [1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 9]
        (results1, results2, results3) = pairs(ARRAY)

        assert results1 == [(1, 9), (1, 9), (4, 6), (4, 6), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (6, 4), (6, 4), (9, 1), (9, 1)]
        assert results2 == [(1, 9), (4, 6), (5, 5), (6, 4), (9, 1)]
        assert results3 == [(1, 9), (4, 6), (5, 5)]

    def test_straight_array(self):
        ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        (results1, results2, results3) = pairs(ARRAY)

        assert results1 == [(1, 9), (2, 8), (3, 7), (4, 6), (6, 4), (7, 3), (8, 2), (9, 1)]
        assert results2 == [(1, 9), (2, 8), (3, 7), (4, 6), (6, 4), (7, 3), (8, 2), (9, 1)]
        assert results3 == [(1, 9), (2, 8), (3, 7), (4, 6)]

    def test_reversed_array(self):
        ARRAY = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        (results1, results2, results3) = pairs(ARRAY)

        assert results1 == [(1, 9), (2, 8), (3, 7), (4, 6), (6, 4), (7, 3), (8, 2), (9, 1)]
        assert results2 == [(1, 9), (2, 8), (3, 7), (4, 6), (6, 4), (7, 3), (8, 2), (9, 1)]
        assert results3 == [(1, 9), (2, 8), (3, 7), (4, 6)]

    def test_crazy_eights(self):
        ARRAY = [8, 8, 8, 8, 8, 8, 8, 8, 2]
        (results1, results2, results3) = pairs(ARRAY)

        assert results1 == [(2, 8), (2, 8), (2, 8), (2, 8), (2, 8), (2, 8), (2, 8), (2, 8), (8, 2), (8, 2), (8, 2), (8, 2), (8, 2), (8, 2), (8, 2), (8, 2)]
        assert results2 == [(2, 8), (8, 2)]
        assert results3 == [(2, 8)]

    def test_doubles(self):
        ARRAY = [1, 1, 9, 9]
        (results1, results2, results3) = pairs(ARRAY)

        assert results1 == [(1, 9), (1, 9), (1, 9), (1, 9), (9, 1), (9, 1), (9, 1), (9, 1)]
        assert results2 == [(1, 9), (9, 1)]
        assert results3 == [(1, 9)]

    def test_triples(self):
        ARRAY = [3, 3, 3, 7, 7, 7]
        (results1, results2, results3) = pairs(ARRAY)

        assert results1 == [(3, 7), (3, 7), (3, 7), (3, 7), (3, 7), (3, 7), (3, 7), (3, 7), (3, 7), (7, 3), (7, 3), (7, 3), (7, 3), (7, 3), (7, 3), (7, 3), (7, 3), (7, 3)]
        assert results2 == [(3, 7), (7, 3)]
        assert results3 == [(3, 7)]

    def test_fives(self):
        ONE_FIVE = [5]
        (results1, results2, results3) = pairs(ONE_FIVE)

        assert results1 == []

        TWO_FIVES = [5, 5]
        (results1, results2, results3) = pairs(TWO_FIVES)

        assert results1 == [(5, 5)] * 2

        THREE_FIVES = [5, 5, 5]
        (results1, results2, results3) = pairs(THREE_FIVES)

        assert results1 == [(5, 5)] * 6

        FOUR_FIVES = [5, 5, 5, 5]
        (results1, results2, results3) = pairs(FOUR_FIVES)

        assert results1 == [(5, 5)] * 12

        FIVE_FIVES = [5, 5, 5, 5, 5]  # 5 5's!
        (results1, results2, results3) = pairs(FIVE_FIVES)

        assert results1 == [(5, 5)] * 20
