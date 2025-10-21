class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = str(2 * n)
        n3 = str(3 * n)
        num = str(n)
        
        num = num + n2 + n3

        mp = {}
        for i in num:
            mp[i] = mp.get(i, 0) + 1

        if '0' in mp:
            return False

        s = 0
        for k, v in mp.items():
            if v != 1:
                return False

        return len(mp) == 9
