class Solution:
    def reformat(self, s: str) -> str:
        dig, let = [i for i in s if i.isnumeric()], [i for i in s if i.isalpha()]

        if len(dig) > len(let) + 1 or len(let) > len(dig) + 1:
            return ""

        if len(dig) < len(let):
            dig, let = let, dig

        res = ""
        for i in range(len(dig) + len(let)):
            if i % 2 == 0:
                res += dig[i//2]
            else:
                res += let[i//2]
        
        return res
