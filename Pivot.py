class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        x = sum(nums)

        sumSoFar = 0
        for i in range(len(nums)):
            if sumSoFar == x - nums[i] - sumSoFar:
                return i
            
            else:
                sumSoFar += nums[i]

        return -1
