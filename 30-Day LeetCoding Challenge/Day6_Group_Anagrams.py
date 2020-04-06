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
