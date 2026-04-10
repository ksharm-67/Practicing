class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3: return -1

        mp = {}
        minDist = math.inf

        for i in range(len(nums)):
            # number: [count, [indices]]
            if nums[i] not in mp:
                mp[nums[i]] = [1, [i]]
            else:
                mp[nums[i]][0] += 1
                mp[nums[i]][1].append(i)

        for val in mp.values():
            indices = val[1]
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    a, b, c = indices[i], indices[i+1], indices[i+2]
                    distance = abs(a - b) + abs(b - c) + abs(c - a)
                    minDist = min(minDist, distance)

    
        return minDist if minDist != math.inf else -1
