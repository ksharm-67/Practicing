class Solution:
    def minimumChairs(self, s: str) -> int:
        
        most = 0
        
        people = 0
        for i in s:
            if i == 'E':
                people += 1
            else:
                people -= 1
            
            most = max(most, people)

        return most