# https://leetcode.com/problems/two-sum/description/

class Solution:

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target - nums[i] == nums[j]:
                    result.append(i)
                    result.append(j)
        return result


s = Solution()
r = s.two_sum([2, 7, 11, 13], 9)
print(r)
r = s.two_sum([3, 2, 4], 6)
print(r)
r = s.two_sum([3, 3], 6)
print(r)
