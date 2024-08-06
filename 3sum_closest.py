class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('-inf')
        for i in range(len(nums)):
            curr = nums[i]
            a,b = i+1,len(nums)-1
            while a<b:
                if abs(nums[i] + nums[a] + nums[b] - target) < abs(closest-target):
                    closest = nums[i] + nums[a] + nums[b]
                if nums[i] + nums[a] + nums[b] - target < 0:
                    a += 1
                elif nums[i] + nums[a] + nums[b] - target > 0:
                    b -= 1
                else:
                    a += 1
                    b -= 1
        return closest                