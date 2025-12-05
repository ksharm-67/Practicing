class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        buckets = [0 for _ in range(max(citations) + 1)]

        for i in citations:
            buckets[i] += 1

        total = 0
        for i in range(len(buckets) - 1, -1, -1):
            total += buckets[i]
            if total >= i:
                return i

        return 0
