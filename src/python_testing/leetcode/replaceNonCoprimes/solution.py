#https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
from math import gcd
from collections import deque
from typing import List


class solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        dq = deque([nums[0]])

        for num in nums[1:]:
            while dq and num > 1:
                top = dq[-1]
                common_divisor = gcd(top, num)

                if common_divisor == 1:
                    break
                else:
                    num = (num * top) // common_divisor
                    dq.pop()

            dq.append(num)

        return list(dq)
