#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def findnum(num, node):
            if not node:
                return 0
            num = num * 10 + node.val
            if not node.left and not node.right:
                return num
            else:
                return findnum(num, node.left) + findnum(num, node.right)

        return findnum(0, root)
        
# @lc code=end

