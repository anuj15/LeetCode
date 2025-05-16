class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        s = s.lower().strip()
        for i in s:
            if i.isalnum():
                res += i
        return res == res[::-1]

s = Solution()
r = s.isPalindrome("A man, a plan, a canal: Panama")
print(r)
r = s.isPalindrome("race a car")
print(r)
r = s.isPalindrome(" ")
print(r)
r = s.isPalindrome("A ssdman, a plan,324 a canal:23 Panama")
print(r)
r = s.isPalindrome("0P")
print(r)