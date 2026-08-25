class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        present = [-1 for i in range(1 + (max(nums) // k))]
        
        for i in nums:
            if i % k == 0:
                present[i // k] = i
        
        for i in range(1, len(present)):
            if present[i] == -1:
                return k * i
            
        return k * len(present)
