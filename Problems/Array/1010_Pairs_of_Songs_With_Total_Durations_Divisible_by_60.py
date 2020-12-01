"""
Runtime: 188 ms, faster than 80.86% of Python online submissions for Pairs of Songs With Total Durations Divisible by 60.
Memory Usage: 16.1 MB, less than 68.82% of Python online submissions for Pairs of Songs With Total Durations Divisible by 60.
"""

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        counter = collections.defaultdict(int)
        res = 0
        for t in time:
            res += counter[(60-t)%60]
            counter[t%60] += 1
        return res
