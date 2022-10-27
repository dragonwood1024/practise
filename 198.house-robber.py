#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        pre1, pre2 = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            cur = max(pre2, pre1+nums[i])
            pre1, pre2 = pre2, cur
        return pre2
        
# @lc code=end

