class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1]) # sort by ending index
        n = len(intervals)
        curr_end = intervals[0][1] # current interval end
        count = n - 1 # assume to start that all intervals are non-overlapping

        for i in range(1, n):
            if intervals[i][0] >= curr_end: # if intervals[i] overlaps current interval end
                curr_end = intervals[i][1] # expand current interval
                count -= 1 # discard intervals[i] from the count

        return count