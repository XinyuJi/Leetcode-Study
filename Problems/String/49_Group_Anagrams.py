"""
Runtime: 196 ms, faster than 5.87% of Python3 online submissions for Group Anagrams.
Memory Usage: 17 MB, less than 37.74% of Python3 online submissions for Group Anagrams.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in dictionary:
                dictionary[key] = [i]
            else:
                dictionary[key].append(i)
        return dictionary.values()


"""
Runtime: 152 ms, faster than 10.13% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.6 MB, less than 30.19% of Python3 online submissions for Group Anagrams.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in sorted(strs):
            key = tuple(sorted(i))
            dictionary[key] = dictionary.get(key, []) + [i]
        return dictionary.values()
