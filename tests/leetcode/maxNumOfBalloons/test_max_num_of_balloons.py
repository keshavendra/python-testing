import unittest

from src.python_testing.leetcode.maxNumOfBalloons.Solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    def test_max_number_of_balloons(self):
        test_cases = [
            ("nlaebolko", 1),
            ("loonbalxballpoon", 2),
            ("leetcode", 0),
            ("balon", 0)
        ]

        for text, expected_result in test_cases:
            actual_result = self.solution.maxNumberOfBalloons(text)
            self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
