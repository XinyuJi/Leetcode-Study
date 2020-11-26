"""
Runtime: 40 ms, faster than 6.98% of Python3 online submissions for Remove Comments.
Memory Usage: 14.3 MB, less than 32.77% of Python3 online submissions for Remove Comments.
"""

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        return filter(None, re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n'))
