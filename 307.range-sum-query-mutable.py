#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (len(nums)+1)
        for i, num in enumerate(nums, 1):
            self.add(i, num)
    
    def add(self, index, value):
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def prefix_sum(self, index):
        val = 0
        while index:
            val += self.tree[index]
            index &= index - 1
        return val

    def update(self, index: int, val: int) -> None:
        difference = val - self.nums[index]
        self.nums[index] = val
        self.add(index+1, difference)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum(right+1) - self.prefix_sum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

