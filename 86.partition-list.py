#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        res  = less
        more = ListNode()
        link = more
        
        while head:
            if head.val < x:
                less.next = head
                less = head 
            else:
                more.next = head
                more = more.next
            head = head.next
        less.next = link.next
        more.next = None
        
        return res.next
        


        
# @lc code=end

