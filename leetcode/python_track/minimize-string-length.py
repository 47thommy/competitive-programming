class Solution:
    def minimizedStringLength(self, s: str) -> int:
        check={}
        count=len(s)
        for i in range(len(s)):
            if s[i] in check:
                count-=1
                check[s[i]]-=1
            else:
                check[s[i]]=check.get(s[i],0)+1
        return count
                