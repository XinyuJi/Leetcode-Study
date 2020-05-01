class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        d[0] = 1
        sums = 0
        count = 0
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k, 0)
            d[sums] = d.get(sums, 0)+1
        return count
