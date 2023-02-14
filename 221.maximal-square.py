#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        edges = [[0] * cols for _ in range(rows)]
        max_edge = 0

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    edges[i][j] = int(matrix[i][j])
                elif matrix[i][j] == "1":
                    edges[i][j] = min(edges[i-1][j-1], edges[i][j-1], edges[i-1][j]) + 1
                else:
                    edges[i][j] = 0
                max_edge = max(max_edge, edges[i][j])
        
        return max_edge**2


        
# @lc code=end

