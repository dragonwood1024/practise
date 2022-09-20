#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            if num-1 not in nums_set:
                curnum = num
                numlen = 0
                while curnum in nums_set:
                    numlen += 1
                    curnum += 1
                longest = max(longest, numlen)
        return longest


# @lc code=end

