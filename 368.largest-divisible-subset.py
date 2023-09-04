#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        size = [1] * n
        pre = [-1] * n
        max_size = 1
        max_index = 0

        nums.sort()

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and size[j] + 1 > size[i]:
                    size[i] = size[j] + 1
                    pre[i] = j
            if size[i] > max_size:
                max_size = size[i]
                max_index = i
        
        res = []
        while max_size:
            res.append(nums[max_index])
            max_index = pre[max_index]
            max_size -= 1
        
        return res[::-1]


        
# @lc code=end

