class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        def tria(arr):
            if len(arr) == 1:
                return arr[0]

            newNums = [(arr[i] + arr[i + 1]) % 10 for i in range(len(arr) - 1)]
            return tria(newNums)

        return tria(nums)

            
