"""
Runtime: 172 ms, faster than 79.28% of Python3 online submissions for Majority Element.
Memory Usage: 15.3 MB, less than 7.14% of Python3 online submissions for Majority Element.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]
