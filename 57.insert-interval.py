#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        left, right = newInterval
        merged = False
        for li, ri in intervals:
            if li > right:
                if not merged:
                    res.append([left, right])
                    merged = True
                res.append([li, ri])
            if ri < left:
                res.append([li, ri])
            else:
                left = min(li, left)
                right = max(ri, right)
        if not merged:
            res.append([left, right])
        return res

# @lc code=end

