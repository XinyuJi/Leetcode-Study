class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if len(num) == k:
            return '0'
        
        for n in num:
            while k > 0 and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        
        for i in range(k):
            stack.pop()

        return ''.join(stack).lstrip('0') or '0'
