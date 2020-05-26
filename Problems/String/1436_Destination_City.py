"""
Runtime: 48 ms, faster than 95.55% of Python3 online submissions for Destination City.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Destination City.
"""

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = {}
        for i in paths:
            dic[i[0]] = i[1]
        
        for start, dest in paths:
            if dest not in dic.keys():
                return dest
