class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        for price in range(1, len(prices)):
            if prices[price] > prices[price -1]:
                max_profit = max_profit + (prices[price] - prices[price -1])
        return max_profit
