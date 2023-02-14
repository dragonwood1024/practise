#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        h = 0
        node = root
        while node.left:
            h += 1
            node = node.left
        
        l, r= pow(2, h), pow(2, (h+1)) -1

        while l < r:
            node = root
            mid = (l+r+1) // 2
            if self.check(node, mid):
                l = mid
            else:
                r = mid - 1 
        return l
        
    def check(self, node, num):
        for s in bin(num)[3:]:
            if s == "0":
                node = node.left if node.left else None
            else:
                node = node.right if node.right else None
            if not node:
                return False
        return True
        


# @lc code=end

