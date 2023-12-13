from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.checkInn=defaultdict(tuple)
        self.checkOutt=defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInn[id]=(stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation,arrivalTime=self.checkInn[id]
        totalTime=t-arrivalTime
        self.checkOutt[(startStation,stationName)].append(totalTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total=sum(self.checkOutt[(startStation,endStation)])
        avg=total/len(self.checkOutt[(startStation,endStation)])
        return avg
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)