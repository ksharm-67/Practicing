class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        seen = set()

        inNum = False
        temp = ""
        for i in range(len(word)):
            if word[i].isdigit():
                inNum = True
                temp += word[i]
            elif inNum:
                seen.add(int(temp))
                temp = ""
                inNum = False
        
        if word and temp:
            seen.add(int(temp))
        print(seen)

        return len(seen)
                