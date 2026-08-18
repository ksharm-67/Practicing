class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        res = -1
        mp = defaultdict(int)
    
        subs = []
        for i in range(len(nums) - k + 1):
            subs.append(nums[i : i + k])

        for sub in subs:
            seen = set()
            for s in sub:
                if s in seen:
                    continue
                else:
                    mp[s] += 1
                    seen.add(s)

        for k, v in mp.items():
            if v == 1:
                res = max(res, k)

        return res
