class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = [1, s.index(i)]
            else:
                dic[i][0] += 1
        index = -1
        for j in dic.values():
            if j[0] == 1:
                index = min(index, j[1])
        if index == -1:
            return -1
        else:
            return index

"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for l in s:
            if l not in d: d[l] = 1
            else: d[l] += 1
        
        index = -1
        for i in range(len(s)):
            if d[s[i]] == 1:
                index = i
                break
        
        return index
"""