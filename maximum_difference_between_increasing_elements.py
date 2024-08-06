class Solution(object):
    def maxDiffAux(nums, lo, hi):
        if len(nums) == 1:
            return nums[0]
        median = floor(len(nums)/2)+1
        print(median) 
    def maximumDifference(self, nums):
        return self.maxDiffAux(0, len(nums))