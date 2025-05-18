class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)

s = Solution()
r = s.removeDuplicates([-1,0,0,0,0,3,3])
print(r)
