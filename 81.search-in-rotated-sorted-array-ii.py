#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        end = n - 1
        if n == 1:
            return target == nums[0]

        for i in range(1, n):
            if nums[i] < nums[i-1]:
                end = i - 1

        if nums[0] <= target <= nums[end] or end == n -1:
            i, j = 0, end
        elif nums[end+1] <= target <= nums[n-1]:
            i, j = end+1, n-1
        else:
            return False
        
        while i <= j:
            idx = (i+j) // 2
            if nums[idx] == target:
                return True
            elif nums[idx] > target:
                j = idx - 1
            else:
                i = idx + 1
        return False

        
# @lc code=end

