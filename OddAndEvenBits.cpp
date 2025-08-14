class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        
        #b = bin(n)[2:]
        binary = bin(n)[2:][::-1]
        
        ev = 0
        od = 0

        for i in range(len(binary)):
            if binary[i] == '1' and i % 2 == 0:
                ev += 1
            elif binary[i] == '1' and i % 2 == 1:
                od += 1
        #print(binary)

        return [ev, od]