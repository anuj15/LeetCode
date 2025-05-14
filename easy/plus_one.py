# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        integer = 0
        new_list = []
        for i in range(len(digits)):
            integer += digits[i] * 10 ** (len(digits) - i - 1)
        integer += 1
        while integer > 0:
            new_list.append(integer % 10)
            integer //= 10
        new_list = new_list[::-1]
        return new_list


s = Solution()
r = s.plusOne([4, 3, 2, 1])
print(r)
