class RandomizedSet:
    def __init__(self):
        self.randset = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.randset)
        self.randset.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        
        loc = self.idx[val]
        last_val = self.randset[-1]

        self.randset[loc] = last_val
        self.idx[last_val] = loc

        self.randset.pop()
        del self.idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.randset)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
