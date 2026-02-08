class Solution:
    def minimumDeletions(self, s: str) -> int:
        indices = {i: [0, 0] for i in range(len(s) + 1)}
        # index: [x, y] where x = Bs before it and y = As after it

        bSoFar = 0
        for i in range(len(s)):
            indices[i][0] = bSoFar
            if s[i] == 'b':
                bSoFar += 1
        indices[len(s)][0] = bSoFar

        aSoFar = 0
        for i in range(len(s) - 1, -1, -1):
            indices[i][1] = aSoFar
            if s[i] == 'a':
                aSoFar += 1
        indices[len(s)][1] = aSoFar
        
        minDel = float('inf')
        for k, v in indices.items():
            minDel = min(minDel, v[0] + v[1])

        return minDel
