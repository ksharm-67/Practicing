class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        cols, wordlen = [], len(strs[0])
        curr = ""
        for i in range(wordlen):
            curr = ""
            for word in strs:
                curr += word[i]
            cols.append(curr)
        
        todel = 0
        for i in cols:
            s = list(i)
            if sorted(s) != s:
                todel += 1
        
        return todel

