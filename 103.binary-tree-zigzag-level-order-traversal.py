#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        nodes = [root]
        direction = True
        while nodes:
            cur_len = len(nodes)
            cur_layer = []
            for _ in range(cur_len):
                cur = nodes.pop(0)
                if direction:
                    cur_layer.append(cur.val)
                else:
                    cur_layer.insert(0, cur.val)
                if cur.left:
                    nodes.append(cur.left)
                if cur.right:
                    nodes.append(cur.right)
            direction = not direction
            res.append(cur_layer)
        return res
        
# @lc code=end

