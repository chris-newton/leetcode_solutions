class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        small = min(strs)
        big = max(strs)
        for i in range(len(small)):
            if small[i] != big[i]:
                return small[:i]
        return small