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
