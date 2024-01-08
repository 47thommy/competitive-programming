class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        ans=0
        check=defaultdict(int)
        if(len(s)==0):
            return 0
        while r<len(s):
            if s[r] in check:
                ans=max(ans,r-l)
                check.pop(s[l])
                l+=1
            else:
                check[s[r]]+=1
                r+=1
        ans=max(ans,r-l)
        return ans
        
                
                
                
            
        
            
            