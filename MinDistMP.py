class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        def reverse(x):
            return int(str(x)[::-1])
        
        mp, res = {}, float('inf')
       
        for i in range(len(nums)):
            rev = reverse(nums[i])
            if nums[i] in mp:
                res = min(res, i - mp[nums[i]])  
            mp[rev] = i

        if res == float('inf'): return -1
        return res
