class Solution:
    def pivotInteger(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        total = n * (n + 1) // 2
        s = 0
        for i in range(1, n + 1):
            s += i
            if total == s:
                return i 
            total -= i

        return -1
