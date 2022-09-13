#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x, y , pre = None, None, None
        
        while root:
            if root.left:
                tmp = root.left
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                if tmp.right is None:
                    tmp.right = root
                    root = root.left
                else:
                    if pre and pre.val > root.val:
                        y = root
                        if not x:
                            x = pre
                    pre = root
                    tmp.right = None
                    root = root.right
            else:
                if pre and pre.val > root.val:
                    y = root
                    if not x:
                        x = pre
                pre = root
                root = root.right
        if x and y:
            x.val, y.val = y.val, x.val



                

# @lc code=end

