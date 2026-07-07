class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        #1 2 0
        #H T O  

        wav = 0
        for i in range(num1, num2 + 1):
            if i < 100:
                continue
            
            num, prev, nxt = i, None, None
            while num >= 100:
                prev = num % 10
                curr = (num // 10) % 10
                nxt = (num // 100) % 10

                if (curr > prev and curr > nxt) or (curr < prev and curr < nxt):
                    wav += 1

                num //= 10

        return wav
