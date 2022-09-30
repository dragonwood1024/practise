#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast:
            if not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None

        
# @lc code=end

