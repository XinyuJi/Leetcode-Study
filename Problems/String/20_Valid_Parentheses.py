"""
Runtime: 28 ms, faster than 72.37% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in dictionary:
                stack.append(i)
            elif len(stack) == 0 or dictionary[stack.pop()]!= i: 
                return False
        return len(stack)==0
