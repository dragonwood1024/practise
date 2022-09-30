#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
        for k in cnt:
            if cnt[k] == 1:
                return k
        
# @lc code=end

