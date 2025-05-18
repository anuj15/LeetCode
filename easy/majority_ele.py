class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        return max(counter, key=counter.get)


s = Solution()
r = s.majorityElement([6, 5, 5])
print(r)
r = s.majorityElement([2, 2, 1, 1, 1, 2, 2])
print(r)
r = s.majorityElement([1])
print(r)
