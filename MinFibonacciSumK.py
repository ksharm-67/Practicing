class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        first, second = 1, 1

        fib = [1]
        while second < k:
            fib.append(first + second)
            first, second = second, second + first

        res, curr = 0, 0
        for i in range(len(fib) - 1, -1, -1):
            if fib[i] > k:
                continue
            if fib[i] + curr == k:
                return res + 1
            if fib[i] + curr < k:
                curr += fib[i]
                res += 1

        return -1
