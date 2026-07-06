class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        sub = 0
        left, right = 0, 0

        while right < len(nums):
            # add the current number to the map
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while freq[nums[right]] > k:
               freq[nums[left]] -= 1
               left += 1

            sub = max(sub, right - left + 1)
            right += 1
        
        return sub

