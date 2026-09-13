class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        res, curr = len(nums), 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                curr += 1
            else: 
                curr = 0
            res += curr
        
        return res
            
