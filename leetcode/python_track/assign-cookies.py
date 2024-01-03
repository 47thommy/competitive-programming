class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gPointer=0
        sPointer=0
        count=0
        while gPointer<len(g) and sPointer<len(s):
            if g[gPointer]<=s[sPointer]:
                count+=1
                sPointer+=1
                gPointer+=1
            elif g[gPointer]>s[sPointer]:
                sPointer+=1
        return count