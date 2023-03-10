#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counter = [0] * (n+1)
        for i in citations:
            if i >= n:
                counter[n] += 1
            else:
                counter[i] += 1
        
        total = 0
        for i in range(n, -1, -1):
            total += counter[i]
            if total >= i:
                return i
        return 0


# @lc code=end

