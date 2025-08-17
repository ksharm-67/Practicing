class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if len(set(nums)) == len(nums) or not nums:
            return 0
        
        ops = 0
        while(len(set(nums)) != len(nums)):
            nums = nums[3:]
            ops += 1

        return ops