class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total=0
        cost=0
        l=0
        while l<len(costs):
            if coins-costs[l]>=0: 
                total+=1
                coins-=costs[l]
            l+=1
        return total