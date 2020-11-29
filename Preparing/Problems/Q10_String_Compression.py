class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        walker = 0
        runner = 0
        
        if len(chars) == 1:
            return 1
        
        while runner < len(chars):
            chars[walker] = chars[runner]
            count = 1
            while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
                count += 1
                runner += 1
            if count > 1:
                for i in str(count):
                    chars[walker+1] = i
                    walker += 1
            
            walker += 1
            runner += 1
            
        return walker


"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        for i in range(len(chars)-1,-1,-1):
            if i and chars[i]==chars[i-1]:
                count += 1
                chars.pop(i)
            else:
                if count>1:
                    for item in str(count)[::-1]:
                        chars.insert(i+1, item)
                    count = 1
"""