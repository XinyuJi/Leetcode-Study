class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        a = m
        i = 1

        while a+i < n+1:
            a &= a+i
            i *= 2
        return a
