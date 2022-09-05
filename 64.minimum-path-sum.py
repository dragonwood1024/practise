#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_sum = [[0]*n for _ in range(m)]
        min_sum[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i-1 >= 0 and j-1 >= 0:
                    min_sum[i][j] = min(min_sum[i-1][j], min_sum[i][j-1]) + grid[i][j]
                elif i-1 >= 0:
                    min_sum[i][j] = min_sum[i-1][j] + grid[i][j]
                elif j-1 >= 0:
                    min_sum[i][j] = min_sum[i][j-1] + grid[i][j]
        
        return min_sum[-1][-1]
        
# @lc code=end

