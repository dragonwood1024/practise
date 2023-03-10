#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1], [1]
        number = len(nums)
        for i in range(1, number):
            prefix.append(prefix[-1]*nums[i-1])
        for i in range(number-2, -1, -1):
            suffix.append(suffix[-1]*nums[i+1])
        res = []
        for i in range(number):
            res.append(prefix[i]*suffix[number-1-i])
        return res
        
# @lc code=end

