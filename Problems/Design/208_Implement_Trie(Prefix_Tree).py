"""
[My Solution] didn't use Trie
Runtime: 1484 ms, faster than 5.01% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 20.2 MB, less than 100.00% of Python3 online submissions for Implement Trie (Prefix Tree).
"""

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.trie.append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.trie:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for i in self.trie:
            if i[0:len(prefix)] == prefix:
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


"""
[Study] Using Trie
Runtime: 132 ms, faster than 91.79% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 26.9 MB, less than 66.67% of Python3 online submissions for Implement Trie (Prefix Tree).
"""

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.dic
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['#'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.dic
        for w in word:
            if w not in cur:
                return False
            else:
                cur = cur[w]
        return '#' in cur
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.dic
        for w in prefix:
            if w not in cur:
                return False
            else:
                cur = cur[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)