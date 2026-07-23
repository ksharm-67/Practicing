class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        res, curr, ori = 0, 0, k

        for i in nums:
            if k < i:
                need = (i - k + ori - 1) // ori
                res += need * curr + (need * (need + 1) // 2)
                curr += need
                k += need * ori
            
            k -= i

        return res % (10**9 + 7)
