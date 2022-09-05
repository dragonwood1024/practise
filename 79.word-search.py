#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def visit(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            used.add((i,j))
            res = False
            for direction in directions:
                if 0 <= direction[0] + i < m and 0 <= direction[1] + j < n:
                    if (direction[0] + i, direction[1] + j) not in used:
                        if visit(direction[0] + i, direction[1] + j, k + 1):
                            res = True
                            break

            used.remove((i,j))
            return res

        m, n = len(board), len(board[0])
        l = len(word)
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        used = set()
        for i in range(m):
            for j in range(n):
                if visit(i, j, 0):
                    return True
        return False

        
# @lc code=end

