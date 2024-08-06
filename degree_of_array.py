class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        
        # store left and right indices of each number
        # store count of each number
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i 
            count[x] = count.get(x, 0) + 1
        
        degree = max(count.values())
        ans = len(nums)
        
        # find minimum range in count with given degree
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans