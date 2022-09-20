#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def subtree(inleft, inright, postleft, postright):
            if postleft > postright:
                return None
            root = postorder[postright]
            rootidx = indices[root]
            node = TreeNode(root)
            sublen = rootidx - inleft

            node.left = subtree(inleft, rootidx-1, postleft, postleft+sublen-1)
            node.right = subtree(rootidx + 1, inright, postleft+sublen,postright-1)

            return node
        
        n = len(inorder)
        indices = {val:idx for idx, val in enumerate(inorder)}
        return subtree(0, n-1, 0, n-1)

        
# @lc code=end

