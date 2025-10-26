class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        
        mp = {}
        for i in s:
            mp[i] = mp.get(i, 0) + 1

        x = sorted(mp.items(), key=lambda x: x[1])
        #print(x)
        
        res = 0
        for i in range(len(x) - k):
            #print("adding: ", x[i][1])
            res += x[i][1]
        
        return res
