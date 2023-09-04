#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.root = 0
        self.res = []
        for i in nestedList:
            self.flatten(i)
    
    def flatten(self, target):
        if target.isInteger():
            self.res.append(target.getInteger())
        else:
            next = target.getList()
            for i in next:
                self.flatten(i)
    
    def next(self) -> int:
        if not self.hasNext():
            return None
        val = self.res[self.root]
        self.root += 1
        return val
    
    def hasNext(self) -> bool:
        return self.root < len(self.res)

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

