class Solution(object):
    def maxSubArray(self, nums):
        partial = summ = float('-inf')
        for i in range(len(nums)):
            partial = max(nums[i], partial + nums[i])
            summ = max(summ, partial)
        return summ