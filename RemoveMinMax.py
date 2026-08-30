class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        minimum, maximum = nums.index(min(nums)), nums.index(max(nums))
        
        # both from left:
        left = max(minimum, maximum) + 1
        
        # both from right:
        right = max(len(nums) - minimum, len(nums) - maximum)

        # one from left and other from right:
        both = min(minimum, maximum) + len(nums) - max(minimum, maximum) + 1

        return min(left, right, both)
