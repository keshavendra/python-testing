from unittest import TestCase
from src.python_testing.canBeTypedWords.Solution import Solution  # Replace 'your_module' with the actual module name


class TestCanBeTypedWords(TestCase):
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    def test_can_be_typed_words(self):
        test_cases = [
            ("leet code", "lt", 1),
            ("hello world", "ad", 1),
            ("leet code", "e", 0),
        ]

        for text, broken_letters, expected_result in test_cases:
            actual_result = self.solution.canBeTypedWords(text, broken_letters)
            self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    import unittest

    unittest.main()
