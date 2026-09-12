class Solution:
    def countHomogenous(self, s: str) -> int:
        res, curr = 1, 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                curr = 1
            res += curr
        
        return res % (10 ** 9 + 7)
