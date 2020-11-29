class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in dic:
                dic[key] = [i]
            else:
                dic[key] += [i]
        return dic.values()
