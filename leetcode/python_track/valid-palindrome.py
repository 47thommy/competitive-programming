class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringf =""
        stringb=""
        for c in s:
            if c.isalnum():
                
                stringf=c+stringf
                stringb=stringb+c
        return stringb.lower()==stringf.lower()
                
        