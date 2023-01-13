#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0   
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
        
# @lc code=end

