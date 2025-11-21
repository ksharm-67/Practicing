class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        seen = {}

        for i in range(len(s) - minSize + 1):
            curr = s[i : i + minSize]

            mp = {}
            for j in curr:
                mp[j] = mp.get(j, 0) + 1

            if len(mp.keys()) <= maxLetters:
                seen[curr] = seen.get(curr, 0) + 1
        
        if not seen:
            return 0
        return max(seen.values())

