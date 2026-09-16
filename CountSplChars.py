class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # letter: [lower, upper]
        mp = {i.lower(): [-1, -1] for i in word}
        
        for i in range(len(word)):
            curr = word[i]
            curr_l = curr.lower()
            if curr.isupper() and mp[curr_l][1] == -1:
                mp[curr_l][1] = i
            elif curr.islower():
                mp[curr_l][0] = i
        
        res = 0
        for k, v in mp.items():
            if v[0] < v[1] and v[1] != -1 and v[0] != -1:
                res += 1
        return res
