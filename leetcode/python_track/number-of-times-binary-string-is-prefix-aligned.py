class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        cmax=0
        count=0
        for i in range(len(flips)):
            cmax=max(cmax,flips[i]-1)
            if i == cmax:
                count+=1
        return count
            