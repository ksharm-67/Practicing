class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ops = 1
        score = 0
        for i in range(0, len(nums) - 1, 2):
            if score == 0:
                score = nums[i] + nums[i + 1]
            elif nums[i] + nums[i + 1] == score:
                ops += 1
            else:
                break
        
        return ops

        
