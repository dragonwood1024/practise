#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        while root:
            if root.left:
                leftend = next = root.left
                while leftend.right:
                    leftend = leftend.right
                root.left = None
                leftend.right = root.right
                root.right = next
            root = root.right

# @lc code=end

