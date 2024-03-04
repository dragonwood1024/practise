#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        current = [0] * 4

        def find(index, start):
            if index == 4 and start == len(s):
                res.append('.'.join(str(addr) for addr in current))
                return

            if index == 4 or start == len(s):
                return

            if s[start] == '0':
                current[index] = '0'
                find(index + 1, start + 1)
                return

            add = 0
            for end in range(start, min(len(s), start + 3)):
                add = add * 10 + ord(s[end]) - ord('0')
                if add <= 255:
                    current[index] = str(add)
                    find(index + 1, end + 1)
        find(0, 0)
        return res

# @lc code=end
