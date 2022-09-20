#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        pre, cur = [0] * n, [0] * n
        
        for i in range(n):
            for j in range(i+1):
                if j == 0:
                    cur[j] = pre[j] + triangle[i][j]
                elif j == i:
                    cur[j] = pre[j-1] + triangle[i][j]
                else:
                    cur[j] = min(pre[j],pre[j-1]) + triangle[i][j]
            pre = cur[:]
        
        return min(cur)
# @lc code=end
