#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.sum = 0
        self.combination = []
        self.find(k, n, 1)
        return self.res
    
    def find(self, size, target, start):
        if self.sum > target:
            return
        if len(self.combination) == size:
            if self.sum == target:
                self.res.append(self.combination[:])
            return
        for i in range(start, 10):
            self.combination.append(i)
            self.sum += i
            self.find(size, target, i+1)
            self.combination.pop()
            self.sum -= i

        
# @lc code=end

