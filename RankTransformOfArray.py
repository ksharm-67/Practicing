class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        n = len(arr)
        res = [0] * n

        ranks, sorted_ranks, curr = {}, sorted(arr), 1
        for i in range(n):
            if sorted_ranks[i] not in ranks:
                ranks[sorted_ranks[i]] = curr            
                curr += 1
        
        for i in range(n):
            res[i] = ranks[arr[i]]

        return res
