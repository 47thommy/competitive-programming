class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        res=[]
        for c in candies:
            temp=c+extraCandies
            if temp>=m:
                res.append(True)
            else:
                res.append(False)
        return res