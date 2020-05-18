"""
Runtime: 100 ms, faster than 90.07% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 14.8 MB, less than 8.70% of Python3 online submissions for Find All Anagrams in a String.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def f(c):
            return ord(c) - 97
        ct_s, ct_p = [0] * 26, [0] * 26
        for c in p:
            ct_p[f(c)] += 1
        l = len(p)
        for c in s[:l-1]:
            ct_s[f(c)] += 1
        res = []
        for i, c in enumerate(s[l-1:]):
            ct_s[f(c)] += 1
            if ct_s == ct_p:
                res.append(i)
            ct_s[f(s[i])] -= 1
        return res

"""
[Solution2: dictionary]
Runtime: 148 ms, faster than 54.89% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 14.8 MB, less than 8.70% of Python3 online submissions for Find All Anagrams in a String.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic_s = collections.Counter(s[:len(p)])
        dic_p = collections.Counter(p)
        i = 0
        j = len(p)
        res = []
        while(j<= len(s)):
            if dic_s == dic_p:
                res.append(i)
            dic_s[s[i]] -= 1
            
            if dic_s[s[i]] <= 0:
                dic_s.pop(s[i])
            
            if j < len(s):
                dic_s[s[j]] += 1
            
            i += 1
            j += 1
        return res
