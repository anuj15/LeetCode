class Solution:
    def hammingWeight(self, n: int) -> int:
        res = []
        while n != 1:
            res.append(n % 2)
            n //= 2
        res.append(n)
        return res.count(1)


s = Solution()
r = s.hammingWeight(2147483645)
print(r)
