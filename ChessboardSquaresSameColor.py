class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:

        col1 = 0           #0 is white, 1 is black
        if ((coordinate1[0] in ['a', 'c', 'e', 'g'] and int(coordinate1[1]) % 2 == 0) or
        coordinate1[0] in ['b', 'd', 'f', 'h'] and int(coordinate1[1]) % 2 == 1):
            col1 = 0
        else:
            col1 = 1

        col2 = 0
        if ((coordinate2[0] in ['a', 'c', 'e', 'g'] and int(coordinate2[1]) % 2 == 0) or
        coordinate2[0] in ['b', 'd', 'f', 'h'] and int(coordinate2[1]) % 2 == 1):
            col2 = 0
        else:
            col2 = 1

        return col1 == col2
        
        
