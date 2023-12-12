class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        ns=s.split(" ")
        s="".join(ns)
        narr=[]
        for n in ns:
            if n!="":
                narr.append(n)
        rnarr=narr[::-1]
        return " ".join(rnarr)
        