class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        least_diff = 0
        for i in prices:
            for j in prices[prices.index(i) + 1:]:
                if i < j:
                    diff = i - j
                    if diff < least_diff:
                        least_diff = diff
        return abs(least_diff)


s = Solution()
r = s.maxProfit([1, 2])
print(r)
r = s.maxProfit([7, 1, 5, 3, 6, 4])
print(r)
r = s.maxProfit([7, 6, 4, 3, 1])
print(r)
