class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            b = list(str(nums[i]))
            c = list(map(int, b))
            if i == sum(c):
                return i

        return -1
