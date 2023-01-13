#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

import collections
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        valid = True
        for p in prerequisites:
            edges[p[1]].append(p[0])

        def dfs(i):
            nonlocal valid
            visited[i] = 1
            for e in edges[i]:
                if visited[e] == 1:
                    valid = False
                    return
                elif visited[e] == 0:
                    dfs(e)

            visited[i] = 2
        
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        return valid


# @lc code=end

