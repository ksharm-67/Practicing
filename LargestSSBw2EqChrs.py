class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mp = {}
        for i in range(len(s)):
            if s[i] in mp:
                mp[s[i]].append(i)
            else:
                mp[s[i]] = [i]

        longest = -1
        for k, v in mp.items():
            if len(v) > 1:
                longest = max(longest, v[-1] - v[0] - 1)
        
        return longest
