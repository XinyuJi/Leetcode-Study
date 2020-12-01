"""
Runtime: 128 ms, faster than 88.13% of Python online submissions for Container With Most Water.
Memory Usage: 15.6 MB, less than 6.68% of Python online submissions for Container With Most Water.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        res, width = 0, len(height)-1
        for w in range(width, 0, -1):
            if height[left] < height[right]:
                res = max(res, height[left] * w)
                left += 1
            else:
                res = max(res, height[right] * w)
                right-= 1
        return res
