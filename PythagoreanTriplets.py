class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        
        for i in range(1, n + 1):
            num = i ** 2
            for j in range(1, i):
                y = sqrt(num - j ** 2)
                if (y > 0 and y < j) and ceil(y) == floor(y):
                    res += 1

        return res * 2

