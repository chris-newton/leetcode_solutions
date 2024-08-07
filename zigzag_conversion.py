class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        ret = ''
        n = len(s)

        for i in range(numRows):
            step1 = numRows*2 - 2 # distance in string between columns
            step2 = i*2 # distance in string between diagonal elts

            for j in range(i, n, step1):
                ret += s[j] # add the char that starts the row

                if step2 > 0 and step2 < step1 and j + step1 - step2 < n:
                    ret += s[j + step1 - step2]
        return ret
