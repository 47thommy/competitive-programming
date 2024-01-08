class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ss1=sorted(s1)
        
        if(len(s1)>len(s2)):
            return False
        for i in range(len(s2)-len(s1)+1):
            if sorted(s2[i:i+len(s1)])==ss1:
                return True
        return False