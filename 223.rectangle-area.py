#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        l = min(ax1, bx1)
        r = max(ax2, bx2)
        u = max(ay2, by2)
        d = min(ay1, by1)
        x = (ax2-ax1) + (bx2-bx1) - (r-l)
        y = (ay2-ay1) + (by2-by1) - (u-d)
        total = (ay2-ay1) * (ax2-ax1)
        total += (by2-by1) * (bx2-bx1)
        if x > 0 and y > 0:
            total -= x*y
        return total
        
# @lc code=end

