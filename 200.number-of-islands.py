#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def set_island(i, j):
            if not 0 <= i < m or not 0 <= j < n:
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
            else:
                return
            set_island(i+1, j)
            set_island(i, j+1)
            set_island(i-1, j)
            set_island(i, j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    set_island(i, j)
        return res
        
# @lc code=end

