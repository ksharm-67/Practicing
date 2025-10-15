class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        
        if income == 0:
            return 0.0

        moneyInBrackets = []
        prev = 0
        for i in range(len(brackets)):
            m = min(income, brackets[i][0]) - prev    
            if m > 0:
                moneyInBrackets.append(min(income, brackets[i][0]) - prev)
            else:
                break
            prev = brackets[i][0]

        tax = 0
        for i in range(len(moneyInBrackets)):
            tax += moneyInBrackets[i] * brackets[i][1]
        return tax / 100
