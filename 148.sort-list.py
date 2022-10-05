#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        def merge(head1, head2):
            temp = ListNode()
            head0 = temp
            while head1 and head2:
                if head1.val < head2.val:
                    head0.next = head1
                    head1 = head1.next
                else:
                    head0.next = head2
                    head2 = head2.next
                head0 = head0.next
            if head1:
                head0.next = head1
            else:
                head0.next = head2
            return temp.next
        
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        
        sublen = 1

        res = ListNode(0,head)
        while sublen < n:
            total = res
            pre = res.next
            while pre:
                head1 = pre
                for _ in range(sublen-1):
                    if pre.next:
                        pre = pre.next
                    else:
                        break
                head2 = pre.next
                pre.next = None
                pre = head2
                for _ in range(sublen-1):
                    if pre and pre.next:
                        pre = pre.next
                    else:
                        break
                next = None
                if pre:
                    next = pre.next
                    pre.next = None
                pre = next

                total.next = merge(head1, head2)
                while total.next:
                    total = total.next
            
            sublen <<= 1
        return res.next
                



        
# @lc code=end

