class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [_ for _ in nums]
        for i in range(len(nums)):
            for x in range(nums[i]):
                if x | (x + 1) == nums[i]:
                    ans[i] = x
                    break
            else:
                ans[i] = -1

        return ans
    
