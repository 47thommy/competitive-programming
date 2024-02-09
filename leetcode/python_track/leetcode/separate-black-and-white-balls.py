class Solution:
    def minimumSteps(self, s: str) -> int:
        count=0
        count_zeros=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="1":
                count+=count_zeros  
            else:
                count_zeros+=1
        return count