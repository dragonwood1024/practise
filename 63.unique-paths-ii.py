#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        steps = [[0] * n for _ in range(m)]
        steps[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    steps[i][j] = 0
                    continue
                if i-1 >= 0:
                    steps[i][j] += steps[i-1][j]
                if j-1 >= 0:
                    steps[i][j] += steps[i][j-1]
        return steps[m-1][n-1]


        
# @lc code=end

