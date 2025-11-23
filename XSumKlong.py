class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
            
        res = [0 for i in range(len(nums) - k + 1)]

        mp = {}
        for i in range(k):
            mp[nums[i]] = mp.get(nums[i], 0) + 1
        
        left, res = 0, [0 for i in range(len(nums) - k + 1)]
        for i in range(len(nums) - k + 1):
            sub = list(mp.items())
            
            klargest = heapq.nlargest(x, sub, key=lambda t: (t[1], t[0]))
            
            x_sum = 0
            for j in klargest:
                x_sum += j[0] * j[1]

            res[i] = x_sum

            if i + k < len(nums):
                mp[nums[i + k]] = mp.get(nums[i + k], 0) + 1
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]

        return res
            


                    
        
