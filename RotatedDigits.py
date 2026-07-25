class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        
        mp = {'0': '0', '1': '1', '8': '8',
              '2': '5', '5': '2',
              '6': '9', '9': '6'}

        for i in range(1, n + 1):
            rotation = list(str(i))
            newNum = [0 for _ in rotation]
            for j in range(len(rotation)):
                if rotation[j] in ['4', '7', '3']:
                    break
                else:
                    newNum[j] = mp[rotation[j]]
            
            else:
                if rotation != newNum:
                    res += 1

        return res
