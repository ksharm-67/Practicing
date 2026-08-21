class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        avgs = [0 if (i > k - 1 and i < len(nums) - k) else -1 for i in range(len(nums))]
        prefix = [0 for _ in range(len(nums) + 1)]

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        prefix[0] = 0
        for i in range(k, len(nums) - k):
            avgs[i] = (prefix[i + k + 1] - prefix[i - k]) // (2 * k + 1)

        return avgs
