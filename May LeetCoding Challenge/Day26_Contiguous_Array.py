class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        count = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count == 0:
                max_len = i + 1
            if count not in dic:
                dic[count] = i
            else:
                max_len = max(i - dic[count], max_len)
        return max_len
