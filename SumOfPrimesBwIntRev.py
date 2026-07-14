class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])
        low, high = min(n, r), max(n, r)   
        
        res = 0
        for i in range(low, high + 1):
            if i == 1:
                continue
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                res += i
        
        return res
