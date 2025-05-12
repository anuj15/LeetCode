# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(s)):
            if i == 0:
                result += d[s[i]]
            elif s[i - 1] == "I" and (s[i] == "V" or s[i] == "X"):
                result += d[s[i]] - d[s[i - 1]] * 2
            elif s[i - 1] == "X" and (s[i] == "L" or s[i] == "C"):
                result += d[s[i]] - d[s[i - 1]] * 2
            elif s[i - 1] == "C" and (s[i] == "D" or s[i] == "M"):
                result += d[s[i]] - d[s[i - 1]] * 2
            else:
                result += d[s[i]]
        return result


s = Solution()
r = s.romanToInt("III")
print(r)
r = s.romanToInt("LVIII")
print(r)
r = s.romanToInt("MCMXCIV")
print(r)
r = s.romanToInt("CDLXIX")
print(r)
