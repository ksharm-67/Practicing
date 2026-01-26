class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if len(arr) <= 2:
            return [arr]

        diffs = max(arr)
        arr.sort()

        for i in range(1, len(arr)):
            diffs = min(diffs, abs(arr[i] - arr[i - 1]))

        res = []
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) == diffs:
                res.append([arr[i - 1], arr[i]])

        return res    
