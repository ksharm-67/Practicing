class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        L = []
        count = 0

        for i in range(len(s) - 2):
            L.append(s[i : i + 3])
        
        for j in L:
            if(len(j) == len(set(j))):
                count += 1

        return count