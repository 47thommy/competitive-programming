from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        ans=0
        odd=0
        for key in count:
           
            if count[key] % 2== 0:
                ans+=count[key]
            else:
                odd+=1
                ans+=count[key]-1
        if odd>0:
            ans+=1
        return ans