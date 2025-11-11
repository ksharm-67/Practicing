class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res, count = 0, 0

        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    count += 1
                if count > (j - i + 1) / 2:
                    res += 1    

        return res
