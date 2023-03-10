#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        val1, val2 = 0, 1
        cnt1, cnt2 = 0, 0
        cnt = len(nums) // 3
        res = []
        for i in nums:
            if i == val1:
                cnt1 += 1
            elif i == val2:
                cnt2 += 1
            else:
                if cnt1 == 0:
                    val1 = i
                    cnt1 += 1
                elif cnt2 == 0:
                    val2 = i
                    cnt2 += 1
                else:
                    cnt1 -= 1
                    cnt2 -= 1
        if nums.count(val1) > cnt:
            res.append(val1)
        if nums.count(val2) > cnt:
            res.append(val2)
        return res

        
# @lc code=end

