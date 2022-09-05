#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(pre, i, temp):
            if i >= len(nums):
                res.append(temp[:])
                return

            dfs(False, i+1, temp)

            if not pre and i-1 >= 0 and nums[i] == nums[i-1]:
                return

            temp.append(nums[i])
            dfs(True, i+1, temp)
            temp.pop()

        res, temp = [], []
        dfs(False, 0, temp)
        return res
        
# @lc code=end

