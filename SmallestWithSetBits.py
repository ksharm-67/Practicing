class Solution:
    def smallestNumber(self, n: int) -> int:

        if n == 1:
            return 1
        
        x = "11"
        for i in range(n):
            if 2 ** i - 1 >= n:
                x = bin(2 ** i - 1)[2:]
                break
        
        return int(x, 2)
