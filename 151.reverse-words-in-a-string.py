#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        n = len(words)
        res = ""
        for i in range(n-1, 0, -1):
            res += words[i] + " "
        res += words[0]
        return res

        
# @lc code=end

