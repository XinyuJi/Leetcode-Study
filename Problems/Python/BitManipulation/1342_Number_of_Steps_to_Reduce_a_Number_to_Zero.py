class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        if num == 0:
            return 0
        else:
            while(num>0):
                if (num % 2) == 0:
                    num = num/2
                    count +=1
                else:
                    num = num -1
                    count +=1
            return count