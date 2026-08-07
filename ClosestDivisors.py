class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        plus_one, plus_two = num + 1, num + 2
        closest = [1, plus_one]
        
        for i in range(1, int(plus_one ** 0.5) + 1):
            div = plus_one // i
            if plus_one % i == 0 and abs(div - i) < (closest[1] - closest[0]):
                closest = [i, div]

        for i in range(1, int(plus_two ** 0.5) + 1):
            div = plus_two // i
            if plus_two % i == 0 and abs(div - i) < (closest[1] - closest[0]):
                closest = [i, div]
            
        return closest
