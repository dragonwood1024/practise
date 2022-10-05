#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eva = []
        op = ["+", "-" , "*", "/"]
        for t in tokens:
            if t in op:
                j = int(eva.pop())
                i = int(eva.pop())

                if t == "+":
                    calc = i + j
                elif t == "-":
                    calc = i - j
                elif t == "*":
                    calc = i * j
                elif t == "/":
                    calc = int(i / j)
                
                eva.append(str(calc))
            else:
                eva.append(t)
        return eva[0]
        
# @lc code=end

