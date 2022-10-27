#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res, sequences = set(), set()
        for i in range(len(s)-9):
            if s[i:i+10] in sequences:
                res.add(s[i:i+10])
            else:
                sequences.add(s[i:i+10])
        return res

        
# @lc code=end

