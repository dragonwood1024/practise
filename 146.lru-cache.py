#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, val, pre=None, next=None):
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
            node.pre.next = node.next
            node.next.pre = node.pre
            self.end.next = node
            node.pre = self.end
            self.end = node
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        tmp = Node(-1)
        new_node = Node(value, self.end, tmp)
        if len(self.position) == self.capacity:
            if self.head.val != -1:
                self.position.pop(self.head.val) 
            self.head = self.head.next
        self.end.next = new_node
        self.end = new_node
        self.position[key] = new_node
        

# @lc code=end

