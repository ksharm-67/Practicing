class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        minDiff, primes = float('inf'), []
        for i in range(max(left, 2), right + 1):
            for j in range(2, isqrt(i) + 1):
                if i % j == 0:
                    break
            else:
                primes.append(i)
        
        #print(primes)
        res = [-1, -1]
        for i in range(len(primes) - 1): 
            currDiff = primes[i + 1] - primes[i]
            if currDiff < minDiff:
                minDiff = currDiff
                res = [primes[i], primes[i + 1]]
            elif currDiff == minDiff:
                if primes[i] < res[0]:
                    res = [primes[i], primes[i + 1]]
            if currDiff == 2:
                return res
        
        return res
