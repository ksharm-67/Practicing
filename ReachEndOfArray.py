class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        score, i = 0, 1
        last = (0, nums[0])

        while i < n:
            if nums[i] > last[1]:
                score += (i - last[0]) * last[1]
                last = (i, nums[i])
            else:
                i += 1
        
        return score + (n - 1 - last[0]) * last[1]

        
