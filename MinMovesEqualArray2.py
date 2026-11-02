class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        
        n = len(nums)
        median = nums[n // 2] if n % 2 != 0 else (nums[(n // 2) - 1] + nums[n // 2]) // 2
        
        res = 0
        for i in nums:
            res += abs(median - i)

        return res
