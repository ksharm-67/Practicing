class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        curr, pos = 0, 0
        for i in nums:
            curr += i
            if curr > 0:
                pos += 1
        
        return pos
