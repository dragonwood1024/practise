#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        second_start_max = (n-1) // 2 + 1
        second_end_max = (n-1)*2 // 3 + 1
        for second_start in range(1, second_start_max+1):
            if num[0] == "0" and second_start != 1:
                break
            for second_end in (second_start, second_end_max+1):
                if num[second_start] == "0" and second_start != second_end:
                    break
                if self.valid(second_start, second_end, num):
                    return True
        return False
    
    def valid(self, second_start, second_end, num):
        n = len(num)
        first_start, first_end = 0, second_start - 1
        while second_end < n:
            third = self.add_num(first_start, first_end, second_start, second_end, num)
            third_len = len(third) 
            if third_len > n - (second_end+1) or num[second_end+1: second_end+1+third_len] != third:
                return False
            if second_end + third_len == n - 1:
                return True
            first_start, first_end = second_start, second_end
            second_start, second_end = second_end + 1, second_end + third_len
    
    def add_num(self, first_start, first_end, second_start, second_end, num):
        carry = 0
        third = []
        while first_end >= first_start or second_end >= second_start or carry != 0:
            cur = 0
            if first_end >= first_start:
                cur += ord(num[first_end]) - ord("0")
            if second_end >= second_start:
                cur += ord(num[second_end]) - ord("0")
            cur += carry
            third.append(str(cur % 10))
            carry = cur // 10
            first_end -= 1
            second_end -= 1
        return "".join(third[::-1])

            

# @lc code=end

