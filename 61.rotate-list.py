#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        chain_len = 1
        node = head
        while node.next:
            node = node.next
            chain_len += 1
        
        node.next = head
        rotates = chain_len - (k % chain_len)

        for _ in range(rotates):
            node = node.next
            head = head.next
        node.next = None

        return head
        
# @lc code=end

