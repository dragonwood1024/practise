#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, s = len(s1), len(s2), len(s3)
        if m+n != s:
            return False
        res = [[False] * (n+1) for _ in range(m+1)]
        res[0][0] = True
        for i in range(m+1):
            for j in range(n+1):
                if i > 0:
                    res[i][j] = (res[i-1][j] and s1[i-1] == s3[i+j-1]) 
                if j > 0:
                    res[i][j] = res[i][j] or (res[i][j-1] and s2[j-1] == s3[i+j-1])
        return res[-1][-1]


# @lc code=end

