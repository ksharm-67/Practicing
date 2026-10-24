class Solution:
    def lexSmallest(self, s: str) -> str:
        if len(s) <= 1:
            return s

        smallest, n = s[:], len(s)
        
        for i in range(1, n + 1):
            x = s[:n - i] + s[n - i:][::-1] 
            y = s[:i][::-1] + s[i:]

            if x < smallest:
                smallest = x
            if y < smallest:
                smallest = y
        
        return smallest

