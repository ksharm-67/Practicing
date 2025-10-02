class Solution:
    def findLucky(self, arr: List[int]) -> int:

        lucky = {}
        for i in range(len(arr)):
            lucky[arr[i]] = lucky.get(arr[i], 0) + 1
                
        res = -1
        for k, v in lucky.items():
            if k == v:
                res = max(res, k)
        
        return res
