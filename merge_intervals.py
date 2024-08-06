class Solution(object):
    def merge(self, intervals):
        ret = []
        for i in sorted(intervals, key=lambda x : x[0]):
            if ret and i[0] <= ret[-1][1]:
                ret[-1][0] = min(i[0], ret[-1][0])
                ret[-1][1] = max(i[1], ret[-1][1])
            else:
                ret.append(i)
        return ret