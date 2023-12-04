class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        f=sum(distance[min(start,destination):max(start,destination)])
              
              
        b=sum(distance)-f
        return min(f,b)
                