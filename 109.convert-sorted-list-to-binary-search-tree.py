#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getlen(node):
            nodelen = 0
            while node:
                nodelen += 1
                node = node.next
            return nodelen
        def build_tree(left, right):
            if left > right:
                return None
            mid = (left+right) // 2
            node = TreeNode()
            node.left = build_tree(left, mid-1)
            nonlocal head
            node.val = head.val
            head = head.next
            node.right = build_tree(mid+1, right)
            return node
        
        nodelen = getlen(head)
        return build_tree(0, nodelen-1)

     
# @lc code=end

