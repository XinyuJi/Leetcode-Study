"""
Runtime: 32 ms, faster than 49.78% of Python3 online submissions for Plus One.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Plus One.
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(int(''.join(map(str,digits)))+1))
