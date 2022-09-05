#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.temp = []
        self.dfs(0, nums)
        return self.ans
    
    def dfs(self, cur, nums):
        if cur == len(nums):
            self.ans.append(self.temp[:])
            return
        self.temp.append(nums[cur])
        self.dfs(cur+1, nums)
        self.temp.pop()
        self.dfs(cur+1, nums)

        
# @lc code=end

