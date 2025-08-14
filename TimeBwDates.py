class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        days1 = 0

        y1 = int(date1[:4])
        m1 = int(date1[5:7])
        d1 = int(date1[8:])

        for i in range(1900, y1):
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0): 
                days1 += 366
            else:
                days1 += 365

        for j in range(1, m1):
            if j == 1 or j == 3 or j == 5 or j == 7 or j == 8 or j == 10 or j == 12:
                days1 += 31
            
            elif j == 2:
                if (y1 % 4 == 0 and y1 % 100 != 0) or (y1 % 400 == 0):
                    days1 += 29
                else:
                    days1 += 28

            elif j == 4 or j == 6 or j == 9 or j == 11:
                days1 += 30
        
        days1 += d1

        days2 = 0

        y2 = int(date2[:4])
        m2 = int(date2[5:7])
        d2 = int(date2[8:])

        for k in range(1900, y2):
            if (k % 4 == 0 and k % 100 != 0) or (k % 400 == 0):
                days2 += 366
            else:
                days2 += 365

        for l in range(1, m2):
            if l == 1 or l == 3 or l == 5 or l == 7 or l == 8 or l == 10 or l == 12:
                days2 += 31
            elif l == 2:
                if (y2 % 4 == 0 and y2 % 100 != 0) or (y2 % 400 == 0):
                    days2 += 29
                else:
                    days2 += 28
            elif l == 4 or l == 6 or l == 9 or l == 11:
                days2 += 30
        
        days2 += d2

        return abs(days2 - days1)
