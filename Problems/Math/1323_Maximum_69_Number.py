"""
Runtime: 24 ms, faster than 86.07% of Python3 online submissions for Maximum 69 Number.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Maximum 69 Number.
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list = list(str(num))
        pos = 10^4
        for i in range(len(num_list)):
            if num_list[i] == "6":
                if i < pos:
                    pos = i
        if pos < len(num_list):
            num_list[pos] = "9"
        return "".join(num_list)
