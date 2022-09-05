#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt, res = 1, len(nums)
        if res == 1:
            return 1
        i = 1
        while i < len(nums) and nums[i] != "_":
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > 2:
                nums.pop(i)
                nums.append("_")
                res -= 1
                i -= 1

            i += 1
        return res

        
# @lc code=end

