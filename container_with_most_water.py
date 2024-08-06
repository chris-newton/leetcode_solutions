class Solution(object):
    def maxArea(self, height):
        most, l, r = 0, 0, len(height)-1
        while l < r:
            most = max(most, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        return most