#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes = [(root, 0)]
        most_rights = {}

        while nodes:
            node, depth = nodes.pop()
            if node:
                most_rights.setdefault(depth, node.val)
                nodes.append((node.left, depth+1))
                nodes.append((node.right, depth+1))
        return [most_rights[i] for i in range(len(most_rights))]

# @lc code=end

