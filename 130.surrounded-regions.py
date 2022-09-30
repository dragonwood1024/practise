#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        n, m = len(board), len(board[0])
        def dfs(x, y):
            if not 0<=x<n or not 0<=y<m or board[x][y]!="O":
                return
            board[x][y] = "C"
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
        
        for i in range(n):
            dfs(i,0)
            dfs(i,m-1)
        for j in range(1, m-1):
            dfs(0, j)
            dfs(n-1, j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "C":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"



# @lc code=end

