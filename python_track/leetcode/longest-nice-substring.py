class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def recurssion(i: int, j: int):
		
            if j - i + 1 < 2: return (0, -1)
            hashset = set()
			
            for k in range(i, j + 1):
                hashset.add(s[k])
            
            for k in range(i, j + 1):
			   
                if s[k].upper() in hashset and s[k].lower() in hashset:
                    continue
			  
                slt = recurssion(i, k - 1)
                srt = recurssion(k + 1, j)
                return slt if (slt[1] - slt[0] + 1) >= (srt[1] - srt[0] + 1) else srt
            return (i, j)
        lt, rt = recurssion(0, len(s) - 1)
        return s[lt:(rt + 1)]