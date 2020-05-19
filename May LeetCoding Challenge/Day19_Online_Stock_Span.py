class StockSpanner:

    def __init__(self):
        self.stack = [(float('inf'), 0)]


    def next(self, price: int) -> int:
        res = 1
        while price >= self.stack[-1][0]:
            res += self.stack.pop()[1]
        self.stack.append((price, res))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
