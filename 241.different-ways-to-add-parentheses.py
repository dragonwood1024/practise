#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i, e in enumerate(expression):
            if e in ["+", "-", "*"]:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if e == "+":
                            res.append(l+r) 
                        elif e == "-":
                            res.append(l-r) 
                        elif e == "*":
                            res.append(l*r) 
        
        return res
        

# @lc code=end

