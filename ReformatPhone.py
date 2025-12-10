class Solution:
    def reformatNumber(self, number: str) -> str:
        
        num, res = number.replace("-", "").replace(" ", ""), ""

        while len(num) > 4:
            res += num[:3]
            num = num[3:]
            if num:               
                res += '-'

        if len(num) <= 3:
            res += num
        else:
            res += num[:2] + '-' + num[2:]

        return res
