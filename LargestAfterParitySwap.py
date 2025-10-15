class Solution:
    def largestInteger(self, num: int) -> int:
        
        odd = []
        even = []
        n = str(num)

        for i in range(len(n)):
            if int(n[i]) % 2 == 0:
                even.append(n[i])
            else:
                odd.append(n[i])

        odd.sort()
        even.sort()

        res = ""
        for i in range(len(odd) + len(even)):
            if int(n[i]) % 2 == 0:
                res += even.pop()
            else:
                res += odd.pop()
        
        return int(res)
