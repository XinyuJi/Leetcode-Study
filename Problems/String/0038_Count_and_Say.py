"""
Runtime: 28 ms, faster than 85.69% of Python online submissions for Count and Say.
Memory Usage: 13.6 MB, less than 27.41% of Python online submissions for Count and Say.
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n-1):
            count = 1
            tmp = []
            for i in range(1, len(s)):
                if s[i-1] == s[i]:
                    count += 1
                else:
                    tmp.extend([str(count), s[i-1]])
                    count = 1
            tmp.extend([str(count), s[-1]])
            s = ''.join(tmp)
        return s
