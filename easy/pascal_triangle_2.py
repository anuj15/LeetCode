class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = []
        row_0 = [1]
        row_1 = [1, 1]
        new_row = []
        res.append(row_0)
        if rowIndex == 0:
            return res[rowIndex]
        res.append(row_1)
        if rowIndex == 1:
            return res[rowIndex]
        else:
            for i in range(rowIndex - 1):
                for j in range(len(res[-1]) - 1):
                    new_row.append(res[-1][j] + res[-1][j + 1])
                new_row.append(1)
                new_row.insert(0, 1)
                res.append(new_row)
                new_row = []
            return res[rowIndex]


s = Solution()
r = s.getRow(0)
print(r)
r = s.getRow(1)
print(r)
r = s.getRow(2)
print(r)
r = s.getRow(3)
print(r)
r = s.getRow(4)
print(r)
r = s.getRow(5)
print(r)
r = s.getRow(6)
print(r)