class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check={}
        left=0
        end=0
        frequency=0
        ans=0
        while end <len(s):
            check[s[end]]=check.get(s[end],0)+1
            frequency=max(frequency, check[s[end]])
            if((end-left+1)-frequency>k):
                
                check[s[left]]-=1
                left+=1
            ans=max(ans,end-left+1)
            end+=1
        return ans
        