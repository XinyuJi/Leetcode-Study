class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    count+=1
        return count
    
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
