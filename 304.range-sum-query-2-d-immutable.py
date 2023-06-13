#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.coner = [[0] * (n+1) for _ in range(m+1)]
        for i in range(0, m):
            for j in range(0, n):
                self.coner[i+1][j+1] = self.coner[i][j+1]\
                    + self.coner[i+1][j] - self.coner[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.coner[row2 + 1][col2 + 1] - self.coner[row2 + 1][col1]\
              - self.coner[row1][col2 + 1] + self.coner[row1][col1]
        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

