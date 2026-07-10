class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefix = []
        s = 0
        for i in arr:
            s += i
            prefix.append(s)
        
        cnt = 0
        for i in range(len(prefix) - k + 1):
            if i == 0:
                if prefix[k - 1] / k >= threshold: 
                    cnt += 1 
            if (prefix[i + k - 1] - prefix[i - 1]) / k >= threshold:
                cnt += 1
            
        return cnt
