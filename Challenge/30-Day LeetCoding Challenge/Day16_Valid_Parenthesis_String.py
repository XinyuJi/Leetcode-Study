class Solution:
    def checkValidString(self, s: str) -> bool:
        max_l = 0
        min_l = 0

        for i in range(len(s)):
            if s[i] == '(':
                max_l += 1
                min_l += 1
            if s[i] == ')':
                max_l -= 1
                if min_l > 0:
                    min_l -= 1
            if s[i] == '*':
                max_l += 1
                if min_l > 0:
                    min_l -= 1
            if max_l < 0:
                return False

        return min_l == 0
