# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)


s = Solution()
r = s.searchInsert([1, 3, 5, 6], 5)
print(r)
r = s.searchInsert([1, 3, 5, 6], 2)
print(r)
r = s.searchInsert([1, 3, 5, 6], 7)
print(r)
