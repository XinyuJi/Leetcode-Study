"""
Runtime: 16 ms, faster than 99.66% of Python online submissions for Minimum Cost For Tickets.
Memory Usage: 13.4 MB, less than 82.43% of Python online submissions for Minimum Cost For Tickets.
"""

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        length = days[-1]+1
        dp_cost = [-1] * length
        dp_cost[0] = 0
        for day in days:
            dp_cost[day] = 0
        for dp_i in range(1, length):
            if dp_cost[dp_i] == -1:
                dp_cost[dp_i] = dp_cost[dp_i - 1]
            else:
                dp_cost[dp_i] = min(dp_cost[dp_i-1]+costs[0], 
                                    dp_cost[max(dp_i-7, 0)]+costs[1], 
                                    dp_cost[max(dp_i -30, 0)]+costs[2] )
        return dp_cost[days[-1]]
