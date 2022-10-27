#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.nodes = []
        while root:
            self.nodes.append(root)
            root = root.left

    def next(self):
        cur = self.nodes.pop()
        node = cur.right
        while node:
            self.nodes.append(node)
            node = node.left
        return cur.val

    def hasNext(self):
        return len(self.nodes) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

