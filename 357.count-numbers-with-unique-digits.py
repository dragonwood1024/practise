#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 10
        if n == 0:
            return 1
        elif n == 1:
            return 10

        for i in range(1, n):
            cur = 9
            for j in range(i):
                cur *= (9-j)
            res += cur

        return res
        
# @lc code=end

