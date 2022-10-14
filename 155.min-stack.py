#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.nums = []
        self.min_list = []

    def push(self, val: int) -> None:
        if not self.nums:
            self.min_list.append(val)
        else:
            self.min_list.append(min(self.min_list[-1], val))
        self.nums.append(val)

    def pop(self) -> None:
        self.nums.pop()
        self.min_list.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.min_list[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

