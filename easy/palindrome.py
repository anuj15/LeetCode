# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


s = Solution()
r = s.isPalindrome(121)
print(r)
r = s.isPalindrome(-121)
print(r)
r = s.isPalindrome(10)
print(r)
