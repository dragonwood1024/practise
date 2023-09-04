#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#

# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        ans = 1
        for x in b:
            ans = pow(ans, 10, mod) * pow(a, x, mod) % mod
        
        return ans
        
# @lc code=end

