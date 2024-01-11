class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        check={}
        left=0
        ans=0
        for end in range(len(fruits)): 
            check[fruits[end]]=check.get(fruits[end],0)+1
            while len(check)>2:
                check[fruits[left]]-=1
                if check[fruits[left]]==0:
                    del check[fruits[left]]
                left+=1
            ans=max(ans,end-left+1)
        return ans