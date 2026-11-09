class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        og_sum = sum([i for i in nums if i % 2 == 0])
        res = [0] * len(queries)

        for i, qu in enumerate(queries):
            idx, val = qu[1], qu[0]
            s = nums[idx] + val

            if nums[idx] % 2 == 0:
                og_sum -= nums[idx]

            nums[idx] += val

            if s % 2 == 0:
                og_sum += s

            res[i] = og_sum

        return res
        
        
            
