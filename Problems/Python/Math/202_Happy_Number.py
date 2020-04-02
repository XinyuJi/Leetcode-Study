class Solution:
    def isHappy(self, n: int) -> bool:
        check_cycle = set()
        while(n != 1):
            n = sum([int(i) **2 for i in str(n)])
            if n in check_cycle:
                return False
            else:
                check_cycle.add(n)
        else:
            return True
