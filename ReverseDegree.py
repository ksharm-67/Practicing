class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        ORD = {chr(k): 123 - k for k in range(97, 123)}

        for i in range(len(s)):
            res += (i + 1) * ORD[s[i]]

        return res
