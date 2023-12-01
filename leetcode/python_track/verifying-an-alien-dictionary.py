class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        check={}
        index=0
        indexCheck=[]
        for c in order:
            check[c]=index
            index+=1
        for i in range(len(words)):
            temp=[]
            for c in words[i]:
                temp.append(check[c])
            indexCheck.append(temp)
        print(indexCheck)
            
        l=0
        while l<=len(words)-2:
            d=0
            while d<min(len(words[l]),len(words[l+1])):
                if check[words[l][d]]<check[words[l+1][d]]:
                    break
                if check[words[l][d]]==check[words[l+1][d]]:
                    d+=1
                else:
                    return False
            if d==min(len(words[l]),len(words[l+1])) and len(words[l])>len(words[l+1]):
                return False    
            l+=1
        return True
        
                    
                    
            