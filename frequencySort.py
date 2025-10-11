class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        max_freq = max(freq.values())
        buckets = [[] for i in range(max_freq)]
        
        for key, val in freq.items():
            buckets[val - 1].append(key * val)  
        
        res = ""
        for i in range(len(buckets) - 1, -1, -1):
            res += "".join(buckets[i])

        return res
