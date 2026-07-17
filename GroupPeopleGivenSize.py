class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        buckets = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in buckets:
                buckets[groupSizes[i]] = [i]
            else:
                buckets[groupSizes[i]].append(i)

        res = []
        for size, people in buckets.items():
            curr = []
            for i in range(len(people)):
                curr.append(people[i])
                if len(curr) == size:
                    res.append(curr)
                    curr = []                                    

        return res
