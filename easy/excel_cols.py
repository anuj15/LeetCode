class Solution:
    def convertToTitle(self, columnNumber: int):
        capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                           "S", "T", "U", "V", "W", "X", "Y", "Z"]
        res = ""
        while columnNumber > 26:
            columnNumber -= 1
            n1 = columnNumber % 26
            res += capital_letters[n1]
            columnNumber //= 26
        res += capital_letters[columnNumber - 1]
        return res[::-1]


s = Solution()
r = s.convertToTitle(1)
print(r)
r = s.convertToTitle(28)
print(r)
r = s.convertToTitle(52)
print(r)
r = s.convertToTitle(701)
print(r)
r = s.convertToTitle(2147483647)
print(r)
