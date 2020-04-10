"""
Runtime: 52 ms, faster than 97.71% of Python3 online submissions for Min Stack.
Memory Usage: 17.4 MB, less than 5.36% of Python3 online submissions for Min Stack.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.obj = []
        self.min = []

    def push(self, x: int) -> None:
        self.obj.append(x)
        if self.min:
            self.min.append(min(self.min[-1], x))
        else:
            self.min.append(x)
        
    def pop(self) -> None:
        del self.obj[-1]
        del self.min[-1]
        
    def top(self) -> int:
        return self.obj[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
