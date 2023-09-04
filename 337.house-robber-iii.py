#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.robsub(root))
    
    def robsub(self, node):
        res = [0, 0]
        if not node:
            return res

        left = self.robsub(node.left)
        right = self.robsub(node.right)
        
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = node.val + left[0] + right[0]

        return res
# @lc code=end

