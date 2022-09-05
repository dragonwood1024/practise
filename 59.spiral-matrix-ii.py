#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[-1] * n for _ in range(n)]
        x, y = 0, 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        direction = 0
        for i in range(1,n**2+1):
            res[x][y] = i
            next_x, next_y = x + directions[direction][0], y + directions[direction][1]
            if (not 0 <= next_x < n) or (not 0 <= next_y < n) or (res[next_x][next_y] != -1):
                direction = (direction + 1) % 4
            x, y = x + directions[direction][0], y + directions[direction][1]
        return res

        
# @lc code=end

