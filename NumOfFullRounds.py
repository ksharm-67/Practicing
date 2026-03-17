class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        
        nearestStart = int(loginTime[:2]) * 60 + int(loginTime[3:])
        nearestEnd = int(logoutTime[:2]) * 60 + int(logoutTime[3:])

        if nearestEnd < nearestStart:
            nearestEnd += 1440

        times = [i for i in range(0, 1440 * 2, 15)]
        
        for j in times:
            if j >= nearestStart:
                nearestStart = j
                break
        
        for j in range(len(times) - 1, -1, -1):
            if times[j] <= nearestEnd:
                nearestEnd = times[j]
                break
        
        rounds = 0
        while nearestStart < nearestEnd:
            nearestStart += 15
            rounds += 1
        
        return rounds
