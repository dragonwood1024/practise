#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) >> 1
            mid_next = mid + 1
            if nums[mid] > nums[mid_next]:
                right = mid
            else:
                left = mid + 1
        return left


        
# @lc code=end

