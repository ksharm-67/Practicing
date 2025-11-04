class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l = []

        for i in range(len(arr)):
            if len(l) < k:
                heapq.heappush(l, (-abs(arr[i] - x), -arr[i]))
            elif (abs(arr[i] - x) < -l[0][0]) or (abs(arr[i] - x) == -l[0][0] and arr[i] < -l[0][1]):
                heapq.heappop(l)
                heapq.heappush(l, (-abs(arr[i] - x), -arr[i]))

        return sorted([-j for i, j in l])
