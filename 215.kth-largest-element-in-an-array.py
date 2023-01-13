#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.nums = nums

        for i in range((n-2)//2, -1, -1):
            self.heapify(i, n-1)

        for j in range(k):
            end = n - 1 - j
            self.nums[0], self.nums[end] = self.nums[end], self.nums[0]
            self.heapify(0, end-1)
        return self.nums[-k]

    def heapify(self, root, end):
        node = root * 2 + 1
        while node <= end:
            if node + 1 <= end and self.nums[node+1] > self.nums[node]:
                node += 1
            if self.nums[node] > self.nums[root]:
                self.nums[node], self.nums[root] = self.nums[root], self.nums[node]
                root = node
                node = root * 2 + 1
            else:
                break
# @lc code=end

