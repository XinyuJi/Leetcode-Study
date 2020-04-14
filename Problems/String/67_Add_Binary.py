"""
[My Solution]
Runtime: 32 ms, faster than 61.44% of Python3 online submissions for Add Binary.
Memory Usage: 13.8 MB, less than 5.41% of Python3 online submissions for Add Binary.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        c = ""
        sum = 0
        k = 0

        for i in range(min(len(a), len(b))):
            sum = int(a[i]) + int(b[i])
            if k == 1:
                sum = sum + 1
            if sum == 2:
                c = c + "0"
                k = 1
            elif sum == 3:
                c = c + "1"
                k = 1
            elif sum < 2:
                c = c + str(sum)
                k = 0

                
        if len(a) > min(len(a), len(b)):
            for j in range(min(len(a), len(b)), len(a)):
                if k == 1:
                    sum = int(a[j]) + 1
                else:
                    sum = int(a[j])
                if sum == 2:
                    c = c + "0"
                    k = 1
                elif sum == 3:
                    c = c + "1"
                    k = 1
                elif sum < 2:
                    c = c + str(sum)
                    k = 0
        else:
            for j in range(min(len(a), len(b)), len(b)):
                if k == 1:
                    sum = int(b[j]) + 1
                else:
                    sum = int(b[j])
                if sum == 2:
                    c = c + "0"
                    k = 1
                elif sum == 3:
                    c = c + "1"
                    k = 1
                elif sum < 2:
                    c = c + str(sum)
                    k = 0


        if k == 1:
            c = c + "1"

        return c[::-1]

"""
[bin()]
Runtime: 28 ms, faster than 83.71% of Python3 online submissions for Add Binary.
Memory Usage: 14.1 MB, less than 5.41% of Python3 online submissions for Add Binary.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
