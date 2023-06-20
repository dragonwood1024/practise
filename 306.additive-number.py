#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        self.seq = []
        return self.backtrack(num, [])
    
    def backtrack(self, num, cur):
        if not num:
            return len(cur) > 2
        
        for i in range(1, len(num) + 1):
            if i > 1 and num[0] == '0':
                break
            if len(cur) < 2 or int(num[:i]) == cur[-2] + cur[-1]:
                self.seq.append(int(num[:i]))
                if self.backtrack(num[i:], self.seq):
                    return True
                self.seq.remove(int(num[:i]))
        return False



# @lc code=end

