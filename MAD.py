class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        size = len(nums)
        suffix, prefix = [0] * size, [0] * size
        
        for i in range(size):
            if i == 0:
                prefix[i] = nums[0]
            else:
                prefix[i] = prefix[i - 1] + nums[i]

        for i in range(size - 1, -1, -1):
            if i == size - 1:
                continue
            suffix[i] = suffix[i + 1] + nums[i + 1]
        
        prefix = [prefix[i] // (i + 1) for i in range(len(prefix))]
        suffix = [suffix[i] // (size - i - 1) if i < size -1 else 0 for i in range(size - 1, -1, -1)][::-1]
        
        res = [abs(prefix[i] - suffix[i]) for i in range(size)]
        
        return res.index(min(res))
