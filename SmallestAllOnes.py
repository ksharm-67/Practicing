class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        res, rem = 1, 11 % k
        while res <= k:
            if rem == 0:
                return res + 1

            rem = (rem * 10 + 1) % k
            res += 1

        return -1 
