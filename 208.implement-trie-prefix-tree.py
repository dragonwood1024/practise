#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.data = collections.defaultdict(list)

    def insert(self, word: str) -> None:
        for i in range(len(word)):
            self.data[word[:i+1]].append(word)

    def search(self, word: str) -> bool:
        for i in range(len(word)):
            if word[:i+1] in self.data:
                for w in self.data[word[:i+1]]:
                    if word == w:
                        return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return True if prefix in self.data else False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

