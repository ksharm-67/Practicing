class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        mp, size = Counter(arr), len(arr)
        vals = sorted(mp.values(), reverse=True)

        remaining = size
        removed = 0

        for k in vals:
            remaining -= k
            removed += 1
            if remaining <= size // 2:
                return removed
