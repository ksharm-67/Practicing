class Solution:
    def dayOfYear(self, date: str) -> int:
        num = 0
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year = int(date[:4])

        mn = int(date[5:7]) - 1
        for i in range(0, mn):
            num += months[i]

        num += int(date[8:])

        if ((year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0)) and mn >= 2:
            num += 1
        return num

        