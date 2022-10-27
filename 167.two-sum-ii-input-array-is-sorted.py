#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def find(idx):
            l, r = idx+1, len(numbers)-1
            while l <= r:
                mid = (l+r) // 2
                rest = target - numbers[idx]
                if numbers[mid] == rest:
                    return [idx+1, mid+1]
                elif numbers[mid] < rest:
                    l = mid+1
                elif numbers[mid] > rest:
                    r = mid-1
            return []
        for i in range(len(numbers)):
            res = find(i)
            if res:
                return res
        return []


        
# @lc code=end

