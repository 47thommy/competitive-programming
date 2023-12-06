class Solution:
    def totalMoney(self, n: int) -> int:
        m=n//7
        temp=m
        r=n%7
        total=0
        while m>0:
            total+=(7/2)*(2*(m)+(6))
            m-=1
        total+=(r/2)*(2*(temp+1)+(r-1))
        return int(total)
        