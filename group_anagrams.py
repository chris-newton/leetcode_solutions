class Solution(object):
    def groupAnagrams(self, strs):
        s = {}
        for w in strs:
            key = tuple(sorted(w))
            s[key] = s.get(key, []) + [w]
        return list(s.values())