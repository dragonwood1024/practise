#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        nodes = [root]
        while nodes:
            nodes_sum = len(nodes)
            cur = None
            for _ in range(nodes_sum):
                cur = nodes.pop(0)
                if cur.left:
                    nodes.append(cur.left)
                if cur.right:
                    nodes.append(cur.right)
                cur.next = nodes[0] if nodes else None
            cur.next = None
        return root
        
# @lc code=end

