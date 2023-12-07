class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        total_length=len(s)+len(spaces)
        spaces_set=set(spaces)
        res=""
        l=0
        while l <len(s):
            if l in spaces_set:
                res+=" "
            res+=s[l]
            l+=1
        return res
                
                