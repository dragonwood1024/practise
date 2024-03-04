#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        total = 0
        def add(nums, total):
            nonlocal res
            if total > target:
                return
            elif total == target:
                res += 1
            for i in nums:
                add(nums, total + i)
        
        add(nums, total)
        return res
        
# @lc code=end

