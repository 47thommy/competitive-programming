class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count=0
        while len(piles)>0:
            count+=piles[-2]
            piles.pop(-1)
            piles.pop(-1)
            piles.pop(0)
        return count