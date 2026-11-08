class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        score, curr = 0, 0

        mp = defaultdict(int)
        left, right = 0, 0

        while right < len(nums):
            mp[nums[right]] += 1
            
            while mp[nums[right]] > 1:
                curr -= nums[left]
                mp[nums[left]] -= 1
                left += 1
            
            curr += nums[right]
            score = max(score, curr)
            right += 1

        return max(score, curr)
