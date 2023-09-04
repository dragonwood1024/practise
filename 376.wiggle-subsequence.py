#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        up, down = 1, 1
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                down = up + 1
            if nums[i] > nums[i-1]:
                up = down + 1
        return max(up, down)

        
# @lc code=end

