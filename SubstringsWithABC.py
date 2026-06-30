class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, mp = 0, {'a': 0, 'b': 0, 'c': 0}

        res = 0
        for i in range(len(s)):
            mp[s[i]] += 1
                
            while mp['a'] >= 1 and mp['b'] >= 1 and mp['c'] >= 1:
                res += len(s) - i
                mp[s[left]] -= 1
                left += 1
        
        return res
