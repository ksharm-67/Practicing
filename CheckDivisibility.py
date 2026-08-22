class Solution:
    def checkDivisibility(self, n: int) -> bool:
        curr_sum, curr_prod, og = 0, 1, n
        while n:
            ones = n % 10
            curr_sum += ones
            curr_prod *= ones
            n //= 10

        return og % (curr_sum + curr_prod) == 0
