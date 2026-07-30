class Solution:
    def splitArray(self, nums: List[int]) -> int:
        prefix_left, prefix_right = [0 for _ in nums], [0 for _ in nums]
        left_valid = [False for _ in nums]
        right_valid = [False for _ in nums]

        left_sum, right_sum, size = 0, 0, len(nums)
        for i in range(size):
            left_sum += nums[i]
            right_sum += nums[size - 1 - i]

            prefix_left[i] = left_sum
            prefix_right[size - 1 - i] = right_sum

        left_valid[0] = True
        for i in range(1, size):
            left_valid[i] = left_valid[i - 1] and nums[i] > nums[i - 1]

        right_valid[-1] = True
        for i in range(size - 2, -1, -1):
            right_valid[i] = right_valid[i + 1] and nums[i] > nums[i + 1]

        diff = float('inf')
        for i in range(size - 1):
            if left_valid[i] and right_valid[i + 1]:
                diff = min(diff, abs(prefix_left[i] - prefix_right[i + 1]))

        return diff if diff != float('inf') else -1
