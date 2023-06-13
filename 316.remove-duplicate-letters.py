#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        saved = set()
        end = {}
        for i in range(len(s)):
            end[s[i]] = i
        
        res = []
        for i in range(len(s)):
            if s[i] not in saved:
                while res and ord(s[i]) < ord(res[-1]) and end[res[-1]] > i:
                    saved.remove(res.pop())
                saved.add(s[i])
                res.append(s[i])
        
        return "".join(res)



        
# @lc code=end

