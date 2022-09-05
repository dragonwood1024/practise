#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if len(nums) == 1:
        #     return True
        furthest = 0

        for i in range(len(nums)):
            if furthest < i:
                return False
            furthest = max(furthest, i+nums[i])
            if furthest >= len(nums) - 1:
                return True
        return False
        
# @lc code=end

