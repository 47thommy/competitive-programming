class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix_sum = []
        one = zero = 0
        for c in s:                              
            prefix_sum.append([zero, one])
            if c == '1':
                one += 1
            else:
                zero += 1    
        suffix_sum = []        
        one = zero = 0
        for c in s[::-1]:                          
            suffix_sum.append([zero, one])
            if c == '1':
                one += 1
            else:
                zero += 1    
        suffix_sum = suffix_sum[::-1]                     
        ans = 0
        for i, c in enumerate(s):                 
            if c == '1':
                ans += prefix_sum[i][0] * suffix_sum[i][0]
            else:    
                ans += prefix_sum[i][1] * suffix_sum[i][1]
        return ans