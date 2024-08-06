class Solution(object):
    def productExceptSelf(self, nums):
        zcount = 0
        
        # case: list has 2 or more zeros, output should be all zeros
        for i in nums:
            if i == 0:
                zcount += 1
        if zcount > 1:
            return [0 for i in range(len(nums))]
        
        ret = []
        prod = 1

        # calc product of all nonzero elems
        for i in nums:
            if i != 0:
                prod *= i
        
        # case: list has 1 zero
        if zcount == 1:
            for i in nums:
                if i == 0:
                    ret.append(prod)
                else:
                    ret.append(0)
        # case: list has no zeros
        else:
            for i in nums:
                ret.append(prod/i)
        
        return ret