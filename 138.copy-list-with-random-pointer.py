#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = {}
        def copy(node):
            if not node:
                return node
            if node in visited:
                return visited[node]
            copy_node = Node(node.val, None, None)
            visited[node] = copy_node
            copy_node.next = copy(node.next)
            copy_node.random =  copy(node.random)
            return copy_node
        return copy(head)
        
# @lc code=end

