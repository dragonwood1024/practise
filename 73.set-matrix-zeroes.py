#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        first_col = False

        for i in range(rows):
            if matrix[i][0] == 0:
                first_col = True
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0
        for i in range(rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0
        if first_col:
            for i in range(rows):
                matrix[i][0] = 0

# @lc code=end

