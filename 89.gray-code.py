#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i
        return ans

# @lc code=end

