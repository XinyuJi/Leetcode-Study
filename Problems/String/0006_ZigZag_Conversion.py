"""
Runtime: 32 ms, faster than 99.20% of Python online submissions for ZigZag Conversion.
Memory Usage: 13.5 MB, less than 96.67% of Python online submissions for ZigZag Conversion.
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1  or numRows >= len(s):
            return s
        L = [''] * numRows
        i, step = 0, 1
        
        for x in s:
            L[i] += x
            if i == 0:
                step = 1
            elif i == numRows-1:
                step = -1
            i += step
        return ''.join(L)
