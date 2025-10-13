class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        if p[-1] == '*':
            if p[:-1] in s:
                return True

        if p[0] == '*':
            if p[1:] in s or p[1:] == s:
                return True

        prefix = ""
        for i in p:
            if i == '*':
                break
            prefix += i
        
        suffix = ""
        i = len(p) - 1
        while p[i] != '*':
            suffix += p[i]
            i -= 1
        suffix = suffix[::-1]

        left = 0
        hasPrefix = False
        for i in range(len(s) - len(prefix) + 1):
            if s[i:i+len(prefix)] == prefix:
                hasPrefix = True
                left = i
                break

        hasSuffix = False
        for i in range(len(prefix) + left, len(s) - len(suffix) + 1):
            if s[i:i+len(suffix)] == suffix:
                hasSuffix = True
                break
            
        return hasPrefix and hasSuffix
