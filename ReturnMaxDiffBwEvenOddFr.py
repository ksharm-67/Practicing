class Solution:
    def maxDifference(self, s: str) -> int:

        freq = {}
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

        even = []
        odd = []
        for key, value in freq.items():
            if value % 2 == 0:
                even.append(value)
            else:
                odd.append(value)

        return max(odd) - min(even)