"""
Runtime: 40 ms, faster than 57.74% of Python online submissions for Trapping Rain Water.
Memory Usage: 14.2 MB, less than 68.77% of Python online submissions for Trapping Rain Water.
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        volume = 0
        left, right = 0, len(height)-1
        max_l, max_r = height[left], height[right]
        while left < right:
            max_l, max_r = max(height[left], max_l), max(height[right], max_r)
            if max_l < max_r:
                volume += max_l - height[left]
                left += 1
            else:
                volume += max_r - height[right]
                right -= 1
        return volume
