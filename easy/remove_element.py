# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        return len(nums)


s = Solution()
r = s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(r)
