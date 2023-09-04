#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = Counter(nums)
        return [x[0] for x in numbers.most_common(k)]
# @lc code=end

