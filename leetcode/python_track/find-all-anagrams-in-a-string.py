class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        left = 0
        smap,pmap={},{}
        for i in range(len(p)):
            pmap[p[i]]=1+pmap.get(p[i],0)
            smap[s[i]]=1+smap.get(s[i],0)
        if pmap == smap:
            res=[0]
        else:
            res=[]
                
        for r in range(len(p), len(s)):
            smap[s[r]]=1+smap.get(s[r],0)
            smap[s[left]]-=1
            if(smap[s[left]]==0):
                smap.pop(s[left])
            left+=1
            if(smap==pmap):
                res.append(left)
        return res

            