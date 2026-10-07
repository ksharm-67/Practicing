class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        res, n = 0, len(nums)
        if k == 0:
            return n
        arr = sorted(nums)

        for i in range(n):
            if nums[i] < arr[n - k]:
                res += 1
        
        return res
