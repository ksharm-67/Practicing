class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        res = 0

        for num in nums:
            width = num % 10
            d = floor(num / 10)

            y, curr = 0, d
            for i in range(int(log10(d)) - width + 1):
                y += (curr % 10) * (10 ** i)
                curr //= 10
            
            res += pow(curr, y, (10 ** 9) + 7)

        return res % ((10 ** 9) + 7)
