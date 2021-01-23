"""
Runtime: 32 ms, faster than 87.74% of Python online submissions for Integer to Roman.
Memory Usage: 13.4 MB, less than 43.72% of Python online submissions for Integer to Roman.
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]
