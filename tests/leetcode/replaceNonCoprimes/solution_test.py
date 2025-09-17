import unittest
from src.python_testing.leetcode.replaceNonCoprimes.solution import solution


class TestReplaceNonCoprimes(unittest.TestCase):
    def setUp(self):
        self.solution = solution()

    def test_replace_non_coprimes_empty_list(self):
        self.assertEqual(self.solution.replaceNonCoprimes([]), [])

    def test_replace_non_coprimes_single_element_list(self):
        self.assertEqual(self.solution.replaceNonCoprimes([2]), [2])

    def test_replace_non_coprimes_no_replacement_needed(self):
        self.assertEqual(self.solution.replaceNonCoprimes([2, 3, 5]), [2, 3, 5])

    def test_replace_non_coprimes_with_replacement(self):
        self.assertEqual(self.solution.replaceNonCoprimes([2, 4, 6]), [12])

    def test_replace_non_coprimes_with_multiple_replacements(self):
        self.assertEqual(self.solution.replaceNonCoprimes([2, 4, 6, 8]), [24])


if __name__ == '__main__':
    unittest.main()
