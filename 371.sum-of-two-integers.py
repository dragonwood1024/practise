#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        bits = 0xFFFFFFFF
        a &= bits
        b &= bits

        while b:
            carry = a & b
            a ^= b
            b = (carry << 1) & bits
        
        return a if a < 0x800000 else ~(a^bits)
       
# @lc code=end

