#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def stolen(start, end):
            first = nums[start]
            second = max(first, nums[start+1])
            for i in range(start+2, end):
                first, second = second, max(second, first+nums[i])
            
            return second
        
        if len(nums) < 3:
            return max(nums)
        else:
            return max(stolen(1,len(nums)), stolen(0, len(nums)-1))

# @lc code=end

