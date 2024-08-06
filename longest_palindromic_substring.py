class Solution(object):
    def longestPalindrome(self, s):
        maxLen = 0
        left, right = 0, 0
        
        for i in range(len(s)):
            odd = self.maxLength(s, i, i)
            even = self.maxLength(s, i, i+1)
            best = max(odd, even)
            if best > maxLen:
                maxLen = best
                if best == odd:
                    left = i - best // 2 
                    right = i + best // 2
                else:
                    left = i - best // 2 + 1
                    right = i + best // 2
        return s[left:right+1]
        
    def maxLength(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1