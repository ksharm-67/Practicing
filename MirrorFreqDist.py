class Solution:
    def mirrorFrequency(self, s: str) -> int:
        let = {chr(k): chr(219 - k) for k in range(97, 123)}
        dig = {str(k): str(9 - k) for k in range(0, 10)}
        seen, res = set(), 0
        
        for c in s:
            m = let[c] if c.isalpha() else dig[c]
            if c not in seen and m not in seen:
                res += abs(s.count(c) - s.count(m))
                seen.add(c)
                seen.add(m)
        
        return res
