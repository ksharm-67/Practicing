class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_time = float('inf')
        openp, closedp = 0, customers.count('Y')
        
        penalties = [0 for _ in range(len(customers) + 1)]
        penalties[0] = closedp

        for i in range(len(customers)):
            if customers[i] == 'N':
                openp += 1
            else:
                closedp -= 1 
            penalties[i + 1] = openp + closedp
        
        return penalties.index(min(penalties))
