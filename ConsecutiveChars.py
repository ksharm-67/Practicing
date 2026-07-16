class Solution:
    def maxPower(self, s: str) -> int:
        curr, longest = 0, 0

        for i in range(1, len(s)):
            if curr == 0 and s[i] == s[i - 1]:
                curr = 1
            elif s[i] == s[i - 1]:
                curr += 1
            else:
                longest = max(longest, curr + 1)
                curr = 0 
        
        return max(longest, curr + 1)
