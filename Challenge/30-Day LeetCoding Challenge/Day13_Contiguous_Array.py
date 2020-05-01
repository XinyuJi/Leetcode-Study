class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if nums.count(0) == nums.count(1):
            return len(nums)
        
        dic = {}
        count = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count = count +1
            else:
                count = count -1 
            
            if count == 0:
                max_len = i + 1
            if count not in dic:
                dic[count] = i
            else:
                max_len= max(max_len, i - dic[count])
        return max_len
