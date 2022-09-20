#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res, path = [], []

        def dfs(node, restsum):
            if not node:
                return
            path.append(node.val)
            restsum -= node.val
            if (not node.left) and (not node.right) and (not restsum):
                res.append(path[:])
            dfs(node.left, restsum)
            dfs(node.right, restsum)
            path.pop()
        
        dfs(root, targetSum)
        return res



# @lc code=end

