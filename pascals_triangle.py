def choose(n, k):
    if k == 0: return 1
    return (n * choose(n - 1, k - 1)) / k
 
class Solution(object):
    def generate(self, numRows):
        tri = []
        
        for N in range(0, numRows):
            row  = []
            for K in range(0, N + 1):
                row.append(choose(N, K))
            tri.append(row)
        return tri