#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        res = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n-1, 0, -1):
            for j in range(i+1, n+1):
                res[i][j] = j + res[i][j-1]
                for k in range(i, j):
                    res[i][j] = min(res[i][j], k + max(res[i][k-1], res[k+1][j]))
        return res[1][n]


# @lc code=end

