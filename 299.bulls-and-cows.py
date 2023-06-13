#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_s = [0] * 10
        count_g = [0] * 10
        bulls, cows = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                count_s[int(s)] += 1
                count_g[int(g)] += 1
        for s, g in zip(count_s, count_g):
            cows += min(int(s), int(g))
        return str(bulls) + "A" + str(cows) + "B"

        
# @lc code=end

