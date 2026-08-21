class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x ** 2)
        score, left, right = 0, 0, len(nums) - 1

        for i in range(len(nums)):
            if i % 2 == 0:
                score += nums[right] ** 2
                right -= 1
            else:
                score -= nums[left] ** 2
                left += 1

        return score
