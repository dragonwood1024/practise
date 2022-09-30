#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]
        res, cur = [], []
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                f[i][j] = f[i+1][j-1] and s[i] == s[j]
        
        def dfs(idx):
            if idx == n:
                res.append(cur[:])
                return
            for i in range(idx, n):
                if f[idx][i]:
                    cur.append(s[idx:i+1])
                    dfs(i+1)
                    cur.pop()

        dfs(0)
        return res


# @lc code=end

