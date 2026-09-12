class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        asc, desc = nums[0], sum(nums) - nums[0] - nums[1]

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                # it's the peak
                if asc + nums[i] == desc + nums[i]:
                    return -1
                elif asc + nums[i] > desc + nums[i]:
                    return 0
                else:
                    return 1
            else:
                asc += nums[i]
                desc -= nums[i + 1]
