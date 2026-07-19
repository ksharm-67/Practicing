class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = Counter(arr1)
        res = []

        for i in arr2:
            for j in range(mp[i]):
                res.append(i)
        
        extra = list(set(arr1) - set(arr2))
        for i in sorted(extra):
            for j in range(mp[i]):
                res.append(i)

        return res
