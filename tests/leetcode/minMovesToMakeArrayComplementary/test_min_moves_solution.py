from unittest import TestCase

from src.python_testing.leetcode.minMovesToMakeArrayComplementary.Solution import Solution


class TestMinMoves(TestCase):
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    def test_min_moves_example_case(self):
        actual_result = self.solution.minMoves([1, 2, 4, 3], 4)
        self.assertEqual(1, actual_result)

    def test_min_moves_when_two_changes_are_required(self):
        actual_result = self.solution.minMoves([1, 2, 2, 1], 2)
        self.assertEqual(2, actual_result)

    def test_min_moves_when_array_is_already_complementary(self):
        actual_result = self.solution.minMoves([1, 2, 1, 2], 2)
        self.assertEqual(0, actual_result)

    def test_min_moves_for_larger_mixed_input(self):
        actual_result = self.solution.minMoves([5, 1, 2, 4, 3, 3], 6)
        self.assertEqual(2, actual_result)

    def test_min_moves_for_single_pair(self):
        actual_result = self.solution.minMoves([3, 3], 3)
        self.assertEqual(0, actual_result)


if __name__ == "__main__":
    import unittest

    unittest.main()