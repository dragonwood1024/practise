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
        res = ListNode(0, head)
        left_node = res
        for _ in range(left - 1):
            left_node = left_node.next
        node = left_node.next
        for _ in range(right-left):
            next = node.next
            node.next = next.next
            next.next = left_node.next
            left_node.next = next
        return res.next

        
# @lc code=end

