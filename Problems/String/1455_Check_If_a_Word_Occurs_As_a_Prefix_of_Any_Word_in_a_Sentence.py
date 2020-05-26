"""
Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
"""

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        txt = sentence.split()
        word = len(searchWord)
        for i in range(len(txt)):
            if searchWord in txt[i] and txt[i][0:word] == searchWord:
                return i+1
        return -1
