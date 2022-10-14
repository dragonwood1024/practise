#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        current = numerator % denominator
        if not current:
            return str(numerator // denominator)
        s = []
        indexs = {}

        if (numerator > 0) != (denominator > 0):
            s.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)
        s.append(str(numerator // denominator))
        s.append(".")

        current = numerator % denominator
        while current and current not in indexs:
            indexs[current] = len(s)
            s.append(str((current*10) // denominator))
            current = (current*10) % denominator
        if current:
            s.insert(indexs[current], "(")
            s.append(")")
        return "".join(s)

# @lc code=end

