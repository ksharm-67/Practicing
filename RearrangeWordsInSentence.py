class Solution:
    def arrangeWords(self, text: str) -> str:
        largestBucket = 0
        sentence = text.split()
        for i in sentence:
            largestBucket = max(largestBucket, len(i))

        buckets = [[] for i in range(largestBucket + 1)]
        
        for word in sentence:
            buckets[len(word)].append(word)

        res = ""
        for i in range(len(buckets)):
            if buckets[i]:
                for j in buckets[i]:
                    if not res:
                        res += (j[0].upper() + j[1:] + ' ')
                        continue 
                    if res and j[0].isupper():
                        res += (j[0].lower() + j[1:] + ' ')
                        continue
                    res += (j + ' ')

        return res.rstrip()
