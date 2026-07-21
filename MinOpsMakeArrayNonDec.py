class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ops = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                ops += nums[i] - nums[i + 1]
                
        return ops
