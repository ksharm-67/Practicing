class Solution:
    def secondHighest(self, s: str) -> int:
        
        hasDigits = False 
        dig = []

        for i in range(len(s)):
            if s[i].isdigit():
                hasDigits = True
                dig.append(s[i])
                
        if hasDigits == False:
            return -1
        
        setDig = list(sorted(set(dig)))
        
        if len(setDig) == 1:
            return -1
        else:
            return int(setDig[-2])
    