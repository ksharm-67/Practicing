class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if len(s) - i <= res:
                break
            mp, unique, max_freq = defaultdict(int), 0, 0
            for j in range(i, len(s)):
                if mp[s[j]] == 0:
                    unique += 1
                mp[s[j]] += 1
                max_freq = max(max_freq, mp[s[j]])
                if max_freq * unique == j - i + 1:
                    res = max(res, j - i + 1)
                
        return res
