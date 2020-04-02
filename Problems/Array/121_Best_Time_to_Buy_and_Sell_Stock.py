"""
Runtime: 68 ms, faster than 34.47% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 15.1 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
