class Solution(object):
    def merge(self, nums1, nums2):
        i, j = 0, 0
        merged = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        if i < len(nums1):
            merged.extend(nums1[i:])
        if j < len(nums2):
            merged.extend(nums2[j:])
        return merged
    
    def findMedianSortedArrays(self, nums1, nums2):
        nums = self.merge(nums1, nums2)
        if len(nums) % 2 == 0:
            return (nums[(len(nums)-1) // 2] + nums[(len(nums)-1) // 2 + 1]) / 2.0
        else:
            return nums[len(nums) // 2]