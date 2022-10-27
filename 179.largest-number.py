#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = sorted(map(str, nums), key=cmp_to_key(lambda a,b:int(b+a)-int(a+b)))
        return "0" if res[0] == "0" else "".join(res)
        
# @lc code=end

