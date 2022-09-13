#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        cur = [0]*4

        def dfs(pos, idx):
            if pos == 4:
                if idx == n:
                    ip = ".".join(str(c) for c in cur)
                    res.append(ip)
                return
            if idx == n:
                return
            if s[idx] == "0":
                cur[pos] = 0
                dfs(pos+1, idx+1)
            
            sum = 0
            for i in range(idx, n):
                sum = sum * 10 + int(s[i])
                if 0 < sum <= 0xFF:
                    cur[pos] = sum
                    dfs(pos+1, i+1)
                else:
                    break

        dfs(0, 0)
        return res

        
# @lc code=end

