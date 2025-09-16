# https://leetcode.com/problems/maximum-number-of-words-you-can-type/
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr = set()
        for i in brokenLetters:
            arr.add(i)
        print(arr)
        count = 0
        can_be_written = True
        for i in text :
            if i == ' ':
                if can_be_written:
                    count = count + 1
                can_be_written = True
            else:
                if i in arr :
                    can_be_written = False
        if can_be_written:
            count = count + 1
        return count

