#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = Node(0, head)
        i = 1
        while node:
            if i == left - 1:
                left_node = node
            if i == right + 1:
                right_node = node
            node = node.next
            i += 1
        while
        
# @lc code=end

