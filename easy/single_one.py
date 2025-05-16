class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for index,value in enumerate(nums):
            if nums.count(value) == 1:
                return value
        return 0


s = Solution()
r = s.singleNumber([2,2,1])
print(r)
r = s.singleNumber([4,1,2,1,2])
print(r)
r = s.singleNumber([1])
print(r)
r = s.singleNumber([])
print(r)
