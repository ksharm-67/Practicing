class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        curr = mass

        for ast in asteroids:
            if curr >= ast:
                curr += ast
            else:
                return False
        
        return True
