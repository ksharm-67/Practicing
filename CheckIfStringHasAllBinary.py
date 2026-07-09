class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        mp = {i: False for i in range(2 ** k)}

        for i in range(len(s) - k + 1):
            mp[int(s[i : i + k], 2)] = True
        
        for k, v in mp.items():
            if not v:
                return False
        return True
        
