class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=""
        stnum=str(x)
        for c in stnum:
            rev=c+rev
        if rev==str(x):
            return True
        else:
            return False
        