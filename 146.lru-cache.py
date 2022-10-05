#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, val, pre=None, next=None):
        self.key = -1
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.position = {}
        self.head = Node(-1)
        self.end = Node(-1, self.head)
        self.head.next = self.end
        
    def get(self, key: int) -> int:
        if key in self.position:
            node = self.position[key]
            self.move(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.position:
            node = self.position[key]
            node.val = value
            self.move(node)
            return
        if len(self.position) == self.capacity:
            pop_node = self.head.next
            self.head.next = pop_node.next
            pop_node.next.pre = self.head
            self.position.pop(pop_node.key)
        new_node = Node(value, self.end.pre, self.end)
        new_node.key = key
        self.end.pre.next = new_node
        self.end.pre = new_node
        self.position[key] = new_node
    
    def move(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = self.end
        node.pre = self.end.pre
        self.end.pre.next = node
        self.end.pre = node

        

# @lc code=end

