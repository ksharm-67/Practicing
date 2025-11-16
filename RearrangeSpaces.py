class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        words, spaces = [], 0

        inWord, temp = False, ""
        for i in range(len(text)):
            if text[i] != ' ':
                temp += text[i]
                inWord = True
            
            else:
                spaces += 1
                if inWord:    
                    words.append(temp)
                    temp = ""
                    inWord = False


        if temp and inWord:
            words.append(temp)

        equal = spaces // (len(words) - 1) if len(words) > 1 else 0
        extra = spaces % (len(words) - 1) if len(words) > 1 else spaces

        return (" " * equal).join(words) + (" " * extra)


            
