class Solution:
    def basec(n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]

    
    
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(n,n-1):
            a=basec(n,i)
            return a==a[::-1]