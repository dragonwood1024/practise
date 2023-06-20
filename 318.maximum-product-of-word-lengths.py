#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = [0] * len(words)
        res = 0
        for i in range(len(words)):
            for c in words[i]:
                mask[i] |= 1 << ord(c) - ord('a')
            for j in range(i):
                if not mask[i] & mask[j]:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

# @lc code=end

