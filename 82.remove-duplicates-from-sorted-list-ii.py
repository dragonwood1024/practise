#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove dups from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        res = ListNode(0, head)
        node = res
        cur = head
        dup = 1
        while cur.next:
            if cur.next.val == cur.val:
                dup += 1
            else:
                if dup == 1:
                    node.next = cur
                    node = cur
                dup = 1
            cur = cur.next
        if dup == 1:
            node.next = cur
        else:
            node.next = None
        return res.next
        
# @lc code=end

