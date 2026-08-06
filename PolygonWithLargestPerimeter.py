class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        curr, prefix = 0, []
        for i in nums: 
            curr += i
            prefix.append(curr)
        
        greatest = -1
        for i in range(2, len(prefix)):
            if nums[i] < prefix[i - 1]:
                greatest = prefix[i]

        return greatest        
