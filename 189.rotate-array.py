#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tem = 0
        for _ in range(k):
            tem = nums.pop()
            nums.insert(0, tem)

        
# @lc code=end

