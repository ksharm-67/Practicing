class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mp = {}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = [i]
            else:
                mp[nums[i]].append(i)

        dist = float('inf')
        for num, idx in mp.items():
            if len(idx) < 3:
                continue

            for i in range(len(idx) - 2):
                f, s, t = idx[i], idx[i + 1], idx[i + 2]
                dist = min(dist, 2 * (max(f, s, t) - min(f, s, t)))

        return dist if dist != float('inf') else -1
            
