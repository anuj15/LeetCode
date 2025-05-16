class Solution:
    def generate(self, num: int) -> list[list[int]]:
        res = []
        row_0 = [1]
        row_1 = [1, 1]
        new_row = []
        res.append(row_0)
        res.append(row_1)
        if num == 1:
            return [row_0]
        else:
            for i in range(num-2):
                for j in range(len(res[-1]) - 1):
                    new_row.append(res[-1][j] + res[-1][j + 1])
                new_row.insert(0, 1)
                new_row.append(1)
                res.append(new_row)
                new_row = []
        return res


s = Solution()
r = s.generate(6)
print(r)
