class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        beautiful = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                ss = s[i:j]
                if not beautiful and ss.count('1') == k:
                    beautiful.append(ss)
                elif ss.count('1') == k and len(ss) <= len(beautiful[-1]):
                    beautiful.append(ss)
        
        if not beautiful:
            return ""

        min_len = min([len(x) for x in beautiful])
        return min(i for i in beautiful if len(i) == min_len)
