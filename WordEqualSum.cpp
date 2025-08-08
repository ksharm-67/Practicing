class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        val1 = ""
        for i in firstWord:
            val1 += str(ord(i) - 97)

        val2 = ""
        for j in secondWord:
            val2 += str(ord(j) - 97)

        val3 = ""
        for k in targetWord:
            val3 += str(ord(k) - 97)
        
        if int(val1) + int(val2) == int(val3):
            return True

        return False
        