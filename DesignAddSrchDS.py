class TrieNode:
    def __init__(self):
        self.end = False
        self.child = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.child:
                curr.child[i] = TrieNode()
            curr = curr.child[i]
        
        curr.end = True
        
    def search(self, word: str) -> bool:
        root = self.root

        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                if word[i] == '.':
                    for node in curr.child.values():
                        if dfs(i + 1, node):
                            return True
                    return False
                else:
                    if word[i] not in curr.child:
                        return False
                    curr = curr.child[word[i]]

            return curr.end
        
        return dfs(0, root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
