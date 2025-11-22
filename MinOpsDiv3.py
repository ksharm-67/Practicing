class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        ops = 0

        for i in range(len(nums)):
            temp, x = nums[i], 0
            while temp % 3 != 0:
                temp += 1
                x += 1

            temp2, y = nums[i], 0
            while temp2 % 3 != 0:
                temp2 -= 1
                y += 1
            
            ops += min(x, y)

        return ops
            
