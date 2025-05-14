class Solution:
    def addBinary(self, a: str, b: str) -> str:
        b_a = 0
        b_b = 0
        res = ""
        for i in range(len(a)):
            b_a += int(a[i]) * 2 ** (len(a) - i - 1)
        for i in range(len(b)):
            b_b += int(b[i]) * 2 ** (len(b) - i - 1)
        b_c = b_a + b_b
        if b_c == 0:
            return "0"
        else:
            while b_c > 0:
                res += str(b_c % 2)
                b_c //= 2
            return res[::-1]


s = Solution()
r = s.addBinary("0", "0")
print(r)
