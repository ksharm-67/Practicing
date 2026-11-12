class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 0

        inc, dec = 1, 1
        for i in range(1, len(nums)):
            res = max(res, dec, inc)
            if nums[i] > nums[i - 1]:
                dec = 1
                inc += 1
            elif nums[i] < nums[i - 1]:
                inc = 1
                dec += 1
            else:
                inc, dec = 1, 1

        return max(res, inc, dec)
