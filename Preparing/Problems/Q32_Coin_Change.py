class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [amount+1] * (amount+1)
        res[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    res[i] = min(res[i], res[i-c]+1)
        if res[amount] == amount + 1:
            return -1
        else:
            return res[amount]
