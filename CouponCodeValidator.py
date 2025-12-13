class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        res = []
        for i in range(len(code)):
            if not code[i] or not isActive[i] or businessLine[i] == "invalid":
                continue
            for j in code[i]:
                if not j.isalnum() and j != '_':
                    break
            else:
                res.append((code[i], businessLine[i]))

        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        res.sort(key=lambda x: (order.index(x[1]) if x[1] in order else len(order), x[0]))
        return [x for x, _ in res]
        
