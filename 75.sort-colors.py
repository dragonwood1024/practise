#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx0, idx1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[idx0] = nums[idx0], nums[i]
                if idx0 < idx1:
                    nums[i], nums[idx1] = nums[idx1], nums[i]
                idx0 += 1
                idx1 += 1
            elif nums[i] == 1:
                nums[i], nums[idx1] = nums[idx1], nums[i]
                idx1 += 1

# @lc code=end

