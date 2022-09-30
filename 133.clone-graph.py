#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = {}

        def clonenode(cur):
            if cur in visited:
                return visited[cur]
            clone_node = Node(cur.val, [])
            visited[cur] = clone_node
            for neighbor in cur.neighbors:
                clone_node.neighbors.append(clonenode(neighbor))
            return clone_node

        return clonenode(node)

# @lc code=end

