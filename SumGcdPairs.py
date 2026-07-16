class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = []
        highest = 0
        for i in nums:
            highest = max(highest, i)
            mx.append(highest)

        prefixGcd = [gcd(nums[i], mx[i]) for i in range(len(nums))]
        prefixGcd.sort()
        left, right = 0, len(nums) - 1

        res = 0
        while left < right:
            res += gcd(prefixGcd[left], prefixGcd[right])
            left, right = left + 1, right - 1

        return res

        
