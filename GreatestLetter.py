class Solution:
    def greatestLetter(self, s: str) -> str:
        
        u = set()

        for i in range(len(s) - 1, -1, -1):
            if s[i].isupper():
                u.add(s[i])

        up = sorted(u, reverse=True)
        
        for i in range(len(up)):
            if up[i].lower() in s:
                return up[i]
        
        return ""
