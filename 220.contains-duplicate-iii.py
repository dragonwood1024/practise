#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        bukets = {}
        for i in range(len(nums)):
            index = nums[i] // (valueDiff + 1)
            if index in bukets or\
                ((index - 1) in bukets and abs(bukets[index-1] - nums[i]) <= valueDiff) or \
                    ((index + 1) in bukets and abs(bukets[index+1] - nums[i]) <= valueDiff):
                return True
            bukets[index] = nums[i]
            if i >= indexDiff:
                bukets.pop(nums[i - indexDiff] // (valueDiff + 1))
        return False

# @lc code=end

