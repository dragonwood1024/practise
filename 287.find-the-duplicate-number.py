#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 1
        r = n-1
        res = -1
        while l <= r:
            cnt = 0
            mid = (l+r) // 2
            for i in range(0, n):
                if nums[i] <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
                res = mid
        return res

# @lc code=end
