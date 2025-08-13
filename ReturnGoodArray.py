class Solution:
    def isGood(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return False
        
        nums = sorted(nums)
        #print(nums)
        for i in range(len(nums) - 1):
            #print(f"current index: {i}, current element: {nums[i]}")
            if i + 1 != nums[i]:
                #print(f"WRONG: {nums[i]} != {i}")
                return False

        return nums[len(nums) - 1] == nums[len(nums) - 2]
        
        