#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = 0
                for bi in [i+1, i-1, i]:
                    for bj in [j+1, j-1, j]:
                        if bi == i and bj == j:
                            continue
                        if 0<=bi<=m-1 and 0<=bj<=n-1 and board[bi][bj] > 0:
                            cnt += 1
                if board[i][j] == 0:
                    if cnt == 3:
                        board[i][j] = -1
                elif cnt < 2 or cnt > 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                cu = board[i][j]
                if cu == -1:
                    board[i][j] = 1
                elif cu == 2:
                    board[i][j] = 0

                            

        
# @lc code=end

