#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        nodes = collections.deque()
        nodes.append(root)
        while nodes:
            cur_len = len(nodes)
            cur_layer = []
            for _ in range(cur_len):
                cur =nodes.popleft()
                cur_layer.append(cur.val)
                if cur.left:
                    nodes.append(cur.left)
                if cur.right:
                    nodes.append(cur.right)
            res.append(cur_layer)
        return res


        
# @lc code=end

