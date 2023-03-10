#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        results_exclusive = 0
        for n in nums:
            results_exclusive ^= n
        lsb = results_exclusive & -results_exclusive

        num1, num2 = 0, 0
        for n in nums:
            if n & lsb:
                num1 ^= n
            else:
                num2 ^= n
        return [num1, num2]
            

        
# @lc code=end

