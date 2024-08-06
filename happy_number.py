def isTen(n):
    while n >= 10:
        n = n / 10
    return n == 10
    
class Solution(object):
    def isHappy(self, n):
        mem = set()
    
        while n != 1 or isTen(n):
            digits = [int(a) for a in str(n)]
            n = 0
            
            for i in range(len(digits)):
                n += digits[i] * digits[i]
            if n in mem:
                return False
            else:
                mem.add(n)
        return True