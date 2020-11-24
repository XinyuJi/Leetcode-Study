"""
Runtime: 44 ms, faster than 47.94% of Python online submissions for String Compression.
Memory Usage: 13.6 MB, less than 93.07% of Python online submissions for String Compression.
"""
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
