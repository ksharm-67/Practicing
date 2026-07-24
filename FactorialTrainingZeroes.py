class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return n
        
        c=0
        while(n):
            n//=5
            c+=n
          
        return c
