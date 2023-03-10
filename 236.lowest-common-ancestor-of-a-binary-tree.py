#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        self.find(root, p, q)
        return self.res
    
    def find(self, node, p, q):
        if not node: return False
        left_contain = self.find(node.left, p, q)
        right_contain = self.find(node.right, p, q)
        if left_contain and right_contain:
            self.res = node
        elif (node.val == p.val or node.val == q.val) \
            and (left_contain or right_contain):
            self.res = node
        return left_contain or right_contain or node.val == p.val or node.val == q.val
        
# @lc code=end

