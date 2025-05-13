# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        d = {"{": 1, "[": 2, "(": 3, "}": -1, "]": -2, ")": -3}
        l = []
        if len(s) > 0 and len(s) % 2 == 0:
            for i in s:
                if d[i] > 0:
                    l.append(d[i])
                else:
                    if abs(d[i]) in l and l[-1] == abs(d[i]):
                        l.pop(-1)
                    else:
                        return False
            return len(l) == 0
        else:
            return False


s = Solution()
# r = s.isValid("()")
# print(r)
# r = s.isValid("()[]{}")
# print(r)
# r = s.isValid("(]")
# print(r)
# r = s.isValid("([])")
# print(r)
# r = s.isValid("([)]")
# print(r)
# r = s.isValid("}{")
# print(r)
# r = s.isValid("([}}])")
# print(r)
r = s.isValid("[([]])")
print(r)
