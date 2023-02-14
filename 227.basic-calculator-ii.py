#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "") + "+"
        calc = []
        pre_sign = "+"
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                if pre_sign == "+":
                    calc.append(num)
                elif pre_sign == "-":
                    calc.append(-num)
                elif pre_sign == "*":
                    calc.append(calc.pop()*num)
                elif pre_sign == "/":
                    calc.append(int(calc.pop()/num))
                num = 0
                pre_sign = c

        return sum(calc)
# @lc code=end

