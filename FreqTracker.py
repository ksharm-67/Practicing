class FrequencyTracker:
    def __init__(self):
        self.data = {}
        self.freq = {}

    def add(self, number: int) -> None:
        old = self.data.get(number, 0)

        self.data[number] = old + 1

        if old > 0:
            self.freq[old] = self.freq.get(old, 0) - 1

        self.freq[old + 1] = self.freq.get(old + 1, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number in self.data:
            old = self.data[number]

            self.freq[old] = self.freq.get(old, 0) - 1
            new = old - 1

            if new == 0:
                del self.data[number]
            else:
                self.data[number] = new
                self.freq[new] = self.freq.get(new, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq.get(frequency, 0) > 0
