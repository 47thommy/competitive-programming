class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=word1+word2
        res=""
        l,r=0,len(word1)
        while l <len(word1) and r<len(word):
            res=res+word[l]
            res=res+word[r]
            l+=1
            r+=1
        while l<len(word1):
            res=res+word[l]
            l+=1
        while r<len(word):
            res=res+word[r]
            r+=1
        return res