"""
[My Solution 1]
Runtime: 44 ms, faster than 6.71% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.6 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    count+=1
        return count

"""
[My Solution 2] Hash Table:
Runtime: 36 ms, faster than 11.60% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.7 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic = {}
        for i in J:
            if i not in dic:
                dic[i] = 0

        for j in S:
            if j in dic:
                dic[j] += 1

        count = 0
        for i in dic.values():
            count += i
        
        return count

"""
[Study - oneline solution]
Runtime: 32 ms, faster than 39.24% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.8 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(j) for j in J)
