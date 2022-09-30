#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        f = [False] * (n+1)
        f[0] = True
        for i in range(1, n+1):
            for j in range(0, i+1):
                if f[j] and s[j:i] in words:
                    f[i] = True
        return f[-1]


        
# @lc code=end

