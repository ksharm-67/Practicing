class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        unq = []  
        freq = {}
        for d in digits:
            if d in freq:
                freq[d] += 1
            else:
                freq[d] = 1

        for i in range(100, 1000, 2):
            ones = int(str(i)[-1])
            tens = int(str(i)[-2])
            hunds = int(str(i)[-3])
            if ones in digits:
                if tens in digits:
                    if hunds in digits:
                        ok = True
                        for d in [hunds, tens, ones]:
                            if [hunds, tens, ones].count(d) > digits.count(d):
                                ok = False
                                break
                        if ok:
                            unq.append(hunds*100 + tens*10 + ones)

        return sorted(unq)