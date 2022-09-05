#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        for p in path.split("/"):
            if not p or p == ".":
                continue
            elif p == ".." and path_stack:
                path_stack.pop()
            elif p != "..":
                path_stack.append(p)
        
        return "/" + "/".join(path_stack)
        
# @lc code=end

