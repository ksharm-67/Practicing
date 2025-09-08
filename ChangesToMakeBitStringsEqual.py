class Solution:
    def minChanges(self, n: int, k: int) -> int:

        if n == k:
            return 0

        binN = bin(n)[2:]
        binK = bin(k)[2:]

        length = max(len(binN), len(binK))
        binN = binN.zfill(length)
        binK = binK.zfill(length)

        cnt = 0
        for i in range(len(binN)):
            if binN[i] == '0' and binK[i] == '1':
                return -1 
            elif binN[i] == '1' and binK[i] == '0':
                cnt += 1
                
        return cnt
