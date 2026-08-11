class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        curr, largest = nums[0], 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr += nums[i]
                print(curr)
            else:
                largest = max(largest, curr)
                break

        largest = max(largest, curr)
        while largest in nums:
            largest += 1
        return largest
