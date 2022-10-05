#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        res = ListNode(0,head)
        inserted = head
        cur = inserted.next

        while cur:
            if inserted.val <= cur.val:
                inserted = inserted.next
            else:
                pre = res
                while pre.next.val <= cur.val:
                    pre = pre.next
                inserted.next = cur.next
                cur.next = pre.next
                pre.next = cur
            cur = inserted.next

        return res.next
        
# @lc code=end

