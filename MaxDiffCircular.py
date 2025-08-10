class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        maxDiff = 0

        for i in range(1, len(nums)):
            diff = abs(nums[i] - nums[i - 1])
            if(diff > maxDiff):
                maxDiff = diff

        return max(maxDiff, abs(nums[len(nums) - 1] - nums[0]))