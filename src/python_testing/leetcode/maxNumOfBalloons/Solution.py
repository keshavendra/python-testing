##https://leetcode.com/problems/maximum-number-of-balloons/
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = [0,0,0,0,0]
        for ch in text:
            if ch == 'b':
                freq[0] += 1
            elif ch == 'a':
                freq[1] += 1
            elif ch == 'l':
                freq[2] += 1
            elif ch == 'o':
                freq[3] += 1
            elif ch == 'n':
                freq[4] += 1
        return min(freq[0], freq[1], freq[2]//2, freq[3]//2, freq[4])