class Solution:
    def largestOddNumber(self, num: str) -> str:
        r=len(num)-1
        while len(num)>0:
            if int(num[-1])%2!=0:
                return num
            num=num[:r]
            r-=1
        return ""