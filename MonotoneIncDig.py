class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = str(n)
        num = [int(i) for i in n]

        for i in range(len(n) - 1, 0, -1):
            if num[i] < num[i - 1]:
                num[i - 1] -= 1
                for j in range(i, len(n)):
                    num[j] = 9

        res = ""
        for i in num: res += str(i)
        return int(res)
