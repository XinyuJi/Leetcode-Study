"""
Runtime: 32 ms, faster than 49.78% of Python3 online submissions for Plus One.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Plus One.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(int(''.join(map(str,digits)))+1))


"""
[My Solution] After 3 months from last submission
Runtime: 44 ms, faster than 6.58% of Python3 online submissions for Plus One.
Memory Usage: 13.8 MB, less than 5.13% of Python3 online submissions for Plus One.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in digits:
            string += str(i)

        digit = []
        for i in list(str(int(string)+1)):
            digit.append(int(i))
        return digit
