#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre_status = [0, 0, 0]
        pre_status[0] = -prices[0]
        pre_status[1] = 0
        pre_status[2] = 0
        
        for i in range(1, len(prices)):
            cur_status = [0, 0, 0]
            cur_status[0] = max((pre_status[2] - prices[i]), (pre_status[0]))
            cur_status[1] = pre_status[0] + prices[i]
            cur_status[2] = max(pre_status[1], pre_status[2])
            pre_status = cur_status
        
        return max(pre_status)
# @lc code=end

