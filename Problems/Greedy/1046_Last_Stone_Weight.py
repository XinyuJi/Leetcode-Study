"""
Runtime: 28 ms, faster than 75.00% of Python3 online submissions for Last Stone Weight.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return "".join(str(x) for x in stones)

        while(len(stones) > 1):
            x = sorted(stones)[len(stones)-1]
            y = sorted(stones)[len(stones)-2]
            if x == y:
                stones.remove(x)
                stones.remove(y)
            else:
                stones.append(x-y)
                stones.remove(x)
                stones.remove(y)

        if len(stones) == 1:
            return "".join(str(x) for x in stones)
        else:
            return 0
