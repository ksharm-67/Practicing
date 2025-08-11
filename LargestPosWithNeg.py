class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        great = 0
        for i in nums:
            if i > great:
                if -i in nums:
                    great = i
        
        if great == 0:
            return -1

        return great
        