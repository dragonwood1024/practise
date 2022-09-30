#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            j = 0
            totalgas, totalcost = 0, 0
            while j < n:
                next = (i+j) % n
                totalgas += gas[next]
                totalcost += cost[next]
                if totalgas < totalcost:
                    break
                j += 1
            if j == n:
                return i
            else:
                i += (j+1)
        return -1

        
# @lc code=end

