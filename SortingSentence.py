class Solution:
    def sortSentence(self, s: str) -> str:
        
        L = s.split()
        sortedList = [i for i in range(len(L))]
        
        for i in L:
            index = int(i[-1])
            sortedList[index - 1] = i[:-1]
        
        res = ""
        for j in sortedList:
            res = res + j + " "

            
        return res[:-1]