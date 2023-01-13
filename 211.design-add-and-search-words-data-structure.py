#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        self.childs = [None] * 26
        self.isend = False

    def addWord(self, word: str) -> None:
        node = self
        for s in word:
            i = ord(s) - ord("a")
            if not node.childs[i]:
                node.childs[i] = WordDictionary()
            node = node.childs[i]
        node.isend = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.isend

            i = ord(word[index]) - ord("a")
            if word[index] == ".":
                for child in node.childs:
                    if child and dfs(index+1, child):
                        return True
            else:
                if node.childs[i] and dfs(index+1, node.childs[i]):
                    return True

            return False

        return dfs(0, self)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

