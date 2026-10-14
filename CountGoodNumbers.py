class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # odd options = 4, even options = 5

        even_indices = ceil(n / 2)
        #print(even_indices)
        odd_indices = floor(n / 2)
        #print(odd_indices)

        return pow(5, even_indices, 10**9 + 7) * pow(4, odd_indices, 10**9 + 7) % (10**9 + 7)
