# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/
from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        pair_count = len(nums) // 2
        difference = [0] * (2 * limit + 2)

        for index in range(pair_count):
            left = nums[index]
            right = nums[-index - 1]

            lower_bound = min(left, right) + 1
            upper_bound = max(left, right) + limit
            pair_sum = left + right

            difference[2] += 2

            difference[lower_bound] -= 1
            difference[pair_sum] -= 1
            difference[pair_sum + 1] += 1
            difference[upper_bound + 1] += 1

        min_moves = float("inf")
        running_sum = 0

        for target_sum in range(2, 2 * limit + 1):
            running_sum += difference[target_sum]
            min_moves = min(min_moves, running_sum)

        return min_moves