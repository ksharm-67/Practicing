class UndergroundSystem:

    def __init__(self):
        self.checkins = {}  # id: [station, time]
        self.checkouts = {} # id: [checkout station, duration of trip]
        self.avgTimes = {} # (startStation, endStation) : [avg times] (list of float)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        f = [stationName, t - self.checkins[id][1]]
        self.checkouts[id] = f
        if (self.checkins[id][0], stationName) in self.avgTimes:
            self.avgTimes[(self.checkins[id][0], stationName)].append(f[1])
        else:
            self.avgTimes[(self.checkins[id][0], stationName)] = [f[1]]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t = self.avgTimes[startStation, endStation]
        return sum(t) / len(t)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
