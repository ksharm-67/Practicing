class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 1 and k == 1:
            return [nums[0]]
        
        buckets = [[] for i in range(len(nums) + 1)]

        mp = {}
        for i in nums:
            mp[i] = mp.get(i, 0) + 1

        for key, value in mp.items():
            buckets[value].append(key)

        res = []
        count = 0
        for i in range(len(buckets) - 1, -1, -1):
            if count >= k:
                break
            if buckets[i]:  
                for num in buckets[i]:
                    if count < k:
                        res.append(num)
                        count += 1
                    else:
                        break
            
        return res