class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        sm = nums[0]
        longest = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                sm += nums[i]
            else:
                break
        longest = sm

        st = set(nums)
        while longest in nums:
            print(longest)
            longest += 1
        
        return longest
        
    
