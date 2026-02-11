class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        low, high = 0, len(people) - 1
        minBoats = 0

        while low < high:
            if people[low] + people[high] <= limit:
                minBoats += 1
                low += 1
                high -= 1

            else:
                minBoats += 1
                high -= 1

        if low == high:
            return minBoats + 1
        return minBoats    
        
