class Solution:
    def myAtoi(self, s: str) -> int:       
        s = s.strip()
        neg = False
        startFrom = 0

        if not s:
            return 0

        if s[0] == '-':
            neg = True 
            startFrom = 1 
        if s[0] == '+':
            startFrom = 1  

        res = "0"
        other = False
        for i in range(startFrom, len(s)):
            if s[i] == '0' and not other:
                continue
            if not s[i].isdigit():
                break
            other = True
            res += s[i]

        ans = 0
        if neg:
            ans = -int(res)
        else:
            ans = int(res)
        
        if ans <= -2 ** 31:
            return -2 ** 31
        if ans >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        return ans
    
