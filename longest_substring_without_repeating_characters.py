class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hash = {}
        length = 0
        maxLength = 0
        start = 0
        for end in range(0, len(s)):
            if s[end] in hash.keys():
                start = max(start, hash[s[end]]+1)
                length = max(1, end-start+1)
                hash.update({s[end]: end}) # update mapping to reflect the most recent occurance of s[j]
            else:
                hash[s[end]] = end
                length += 1
            maxLength = max(maxLength, length)
        return maxLength