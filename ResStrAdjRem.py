class Solution:
    def resultingString(self, s: str) -> str:
        stk = []
        if len(s) <= 1: return s

        for i in range(len(s)):
            if stk and (abs(ord(s[i]) - ord(stk[-1])) == 1 or abs(ord(s[i]) - ord(stk[-1])) == 25):
                stk.pop()
            else:
                stk.append(s[i])
        
        return "".join(stk)
