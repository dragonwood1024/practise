#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        subarray_sum = 0
        start, end, res = 0, 0, len(nums)+1
        while end < len(nums):
            subarray_sum += nums[end]
            while subarray_sum >= target:
                res = min(res, end-start+1)
                subarray_sum -= nums[start]
                start += 1
            end += 1
        return 0 if res == len(nums)+1 else res
        
# @lc code=end

