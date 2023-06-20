#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        degree = 1
        for node in preorder.split(','):
            degree -= 1
            if degree < 0:
                return False
            if node != '#':
                degree += 2

        return degree == 0

        
# @lc code=end

