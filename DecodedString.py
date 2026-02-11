class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        totalLen = 0

        for i in range(len(s)):
            if s[i].isalpha():
                totalLen += 1
            else:
                totalLen *= int(s[i])
            if totalLen >= k:  
                break

        for j in range(i, -1, -1):
            if s[j].isalpha() and k == totalLen:
                return s[j]

            elif s[j].isalpha():
                totalLen -= 1

            elif s[j].isnumeric():
                totalLen //= int(s[j])
                k = k % totalLen if k % totalLen != 0 else totalLen

        return ""
