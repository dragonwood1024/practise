#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        concat = []
        for l in matrix:
            concat += l
        n = len(concat)

        i , j = 0, n-1

        while i <= j:
            idx = (i+j+1) // 2
            if concat[idx] == target:
                return True
            elif concat[idx] < target:
                i = idx + 1 
            elif concat[idx] > target:
                j = idx - 1
        return False
        
# @lc code=end

