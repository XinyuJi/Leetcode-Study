class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        if len(arr) < 2:
            return 0
        for i in arr: 
            if i+1 in arr:
                count = count+1
        return count
                