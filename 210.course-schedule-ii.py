#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        search_states = [0] * numCourses
        relations = collections.defaultdict(list)
        res = []
        valid = True

        for p in prerequisites:
            relations[p[1]].append(p[0])
        
        def find(i):
            nonlocal valid
            search_states[i] = 1
            for r in relations[i]:
                if search_states[r] == 0:
                    find(r)
                elif search_states[r] == 1:
                    valid = False
                    return
            search_states[i] = 2
            res.append(i)
        
        for i in range(numCourses):
            if valid and not search_states[i]:
                find(i)
        return res[::-1] if valid else []
        
# @lc code=end

