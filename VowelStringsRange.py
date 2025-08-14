class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        count = 0
        
        vow = ['a', 'e', 'i', 'o', 'u']
        for i in range(left, right + 1):
            if words[i][0] in vow:
                if words[i][-1] in vow:
                    #print(f"Start: {words[i][0]}, end: {words[i][-1]}")
                    count += 1
        
        return count