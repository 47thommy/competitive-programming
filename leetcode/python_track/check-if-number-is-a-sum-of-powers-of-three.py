class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        rem=[]
        while n!=0:
            r = n%3
            n= n//3
            rem.append(r)
        if 2 in rem:
            return False
        else:
            return True