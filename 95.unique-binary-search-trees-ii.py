#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def find(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in  range(start, end+1):
                left_trees = find(start, i-1)
                right_trees = find(i+1, end)
                for l in left_trees:
                    for r in right_trees:
                        node = TreeNode(i, l ,r)
                        all_trees.append(node)
            return all_trees
        return find(1,n) if n else []
        
# @lc code=end

