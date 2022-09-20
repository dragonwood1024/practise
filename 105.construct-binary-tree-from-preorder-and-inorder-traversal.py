#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def subtree(preleft, preright, inleft, inright):
            if preleft > preright:
                return None
            root = preorder[preleft]
            rootidx = indices[root]
            sublen = rootidx - inleft
            node = TreeNode(root)

            node.left = subtree(preleft+1, preleft+sublen, inleft, rootidx-1)
            node.right = subtree(preleft+sublen+1, preright, rootidx+1, inright)

            return node

        n = len(preorder)
        indices = {val : idx for idx, val in enumerate(inorder)}
        return subtree(0, n-1, 0, n-1)

# @lc code=end

