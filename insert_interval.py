class Solution(object):
    def insert(self, intervals, newInterval):
        s, e = newInterval[0], newInterval[1]
        left = [x for x in intervals if x[1] < s]
        right = [x for x in intervals if x[0] > e]
        if left + right != intervals:
            newInterval[0] = min(s, left[-1])
            newInterval[1] = max(newInterval[1], right[-1])
        return left + newInterval + right