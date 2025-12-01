class Solution:
    def stringHash(self, s: str, k: int) -> str:
        
        words = [s[i : i + k] for i in range(0, len(s) - k + 1, k)]
       
        res = ""
        for i in words:
            curr = 0
            for j in i:
                curr += ord(j) - 97
                curr %= 26
            res += chr(curr + 97)
        
        return res
