class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1="qwertyuiop"
        r2="asdfghjkl"
        r3="zxcvbnm"
        ans=[]
        for word in words:
            l=word.lower()
            c1=0
            c2=0
            c3=0
            for i in range(len(l)):
                if l[i] in r1:
                    c1+=1
                if l[i] in r2:
                    c2+=1
                if l[i] in r3:
                    c3+=1
            if c1==len(word) or c2==len(word) or c3==len(word):
                ans.append(word)
                
        return ans
            
            