class Solution(object):
    def trap(self, height):
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maxLeft[0] = height[0]
        maxRight[len(height)-1] = height[len(height)-1]
        vol = 0 # running count of rain cells

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
            
        for i in reversed(range(len(height)-1)):
            maxRight[i] = max(maxRight[i+1], height[i+1])
                    
        for i in range(1, len(height)-1):
            maxLevel = min(maxLeft[i], maxRight[i])
            if height[i] <= maxLevel:
                vol += maxLevel - height[i]
            
        return vol