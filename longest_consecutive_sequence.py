class Solution(object):
    def longestConsecutive(self, nums):
        # add all nums to the set
        # sets are unordered so each add operation is O(1) and the whole loop is O(n)
        s = set()
        for num in nums:
            s.add(num)

        counter = 0
        for num in s:
            # only select starting locations of each consecutive sequence.
            # if num-1 is in s, we are already in the middle of a sequence
            if num-1 not in s: 
                i = 0
                while num+i in s:
                    i += 1
                counter = max(counter, i)
        return counter