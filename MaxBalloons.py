class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        mp, instances = Counter(list(text)), 0
        exitLoop = False

        while True:
            for i in "balloon":
                if mp[i] == 0:
                    exitLoop = True
                    break
                mp[i] -= 1
            instances += 1

            if exitLoop:
                break

        return instances - 1
