class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dic = {}
        self.queue = []
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        while len(self.queue) >0 and self.dic[self.queue[0]] > 1:
            self.queue.pop(0)
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]

    def add(self, value: int) -> None:
        if value not in self.dic:
            self.dic[value] = 1
            self.queue.append(value)
        else:
            self.dic[value] += 1
            
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)