class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = {'a', 'e', 'i', 'o', 'u'}
        res = 0

        for i in range(len(s)):
            curr = 0
            if i < k:
                if s[i] in vow:
                    curr += 1
            else:
                if s[i] in vow:
                    curr += 1
                if s[i - k] in vow:
                    curr -= 1
            res = max(res, curr)
        
        return res
