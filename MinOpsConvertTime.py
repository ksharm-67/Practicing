class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        currH, currM = int(current[:2]), int(current[3:])

        corrH, corrM = int(correct[:2]), int(correct[3:])

        curr, corr = 60 * currH + currM, 60 * corrH + corrM
        
        res = 0
        while curr + 60 <= corr:
            curr += 60
            res += 1
        
        while curr + 15 <= corr:
            curr += 15
            res += 1
        
        while curr + 5 <= corr:
            curr += 5
            res += 1
        
        while curr + 1 <= corr:
            curr += 1
            res += 1
        
        return res

        
