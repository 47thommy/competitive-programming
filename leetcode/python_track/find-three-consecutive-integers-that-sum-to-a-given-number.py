class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n=(num-3)%3
        x=(num-3)//3
        res=[]
        if n==0:
            res.append(x)
            res.append(x+1)
            res.append(x+2)
            return res
        else:
            return res