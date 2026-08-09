class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            curr = 0
            while n:
                curr += (n % 10) ** 2
                n //= 10
            n = curr

            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)

