class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        vowels = [0] * len(words)

        for i, word in enumerate(words):
            vowels[i] = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')
        
        first = vowels[0]
        for i in range(1, len(words)):
            if vowels[i] == first:
                words[i] = words[i][::-1]

        return " ".join(words)
