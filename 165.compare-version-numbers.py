#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        n1, n2 = len(v1), len(v2)
        idx = 0
        while idx < n1 and idx < n2:
            num1 = int(v1[idx])
            num2 = int(v2[idx])
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            idx += 1
        if idx < n1:
            for i in range(idx, n1):
                if int(v1[i]) != 0:
                    return 1
        elif idx < n2:
            for i in range(idx, n2):
                if int(v2[i]) != 0:
                    return -1
        return 0
        
        
# @lc code=end

