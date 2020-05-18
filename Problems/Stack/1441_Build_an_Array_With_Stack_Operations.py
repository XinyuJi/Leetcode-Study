"""
Runtime: 24 ms, faster than 98.56% of Python3 online submissions for Build an Array With Stack Operations.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Build an Array With Stack Operations.
"""

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        n_list = []
        for i in range(1, target[-1]+1):
            n_list.append("Push")
            if i not in target:
                n_list.append("Pop")
        return n_list
