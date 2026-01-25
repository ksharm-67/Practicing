class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        diff = max(nums)

        for i in range(len(nums) - k + 1):
            window = nums[i : i + k]
            diff = min(diff, max(window) - min(window))

        return diff
