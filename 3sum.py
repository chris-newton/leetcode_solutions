class Solution(object):
    def threeSum(self, nums):
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            a = i+1
            b = len(nums)-1

            while a < b:
                sum = nums[i] + nums[a] + nums[b]

                if sum == 0:
                    ans.append([nums[i], nums[a], nums[b]])

                    while a < b and nums[a] == nums[a+1]:
                        a += 1
                    while a < b and nums[b] == nums[b-1]:
                        b -= 1
                        
                    a += 1
                    b -= 1
                elif sum < 0:
                    a += 1
                else:
                    b -= 1
                
        return ans