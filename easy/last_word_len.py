# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

s = Solution()
r = s.lengthOfLastWord("Hello World")
print(r)
