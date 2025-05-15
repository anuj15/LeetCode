class Solution:
    def mySqrt(self, x: int):
        nums = []
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(1, x + 1, 2):
            if x - i < 0:
                return len(nums)
            else:
                x -= i
                nums.append(i)
        return len(nums)


s = Solution()
r = s.mySqrt(2147395599)
print(r)
