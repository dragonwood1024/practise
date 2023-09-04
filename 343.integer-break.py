#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        res *= n
        return res
        
# @lc code=end

