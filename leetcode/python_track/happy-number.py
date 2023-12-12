class Solution:
    def isHappy(self, n: int) -> bool:
        check={}
        flag=True
        ans=0
        while flag:
            temp=[]
            for i in range(len(str(n))):
                r=str(n)[i]
                temp.append(int(r)**2)
            ans=sum(temp)
            print(ans)
            n=ans
            if ans == 1:
                return True
            if ans in check:
                return False
            check[ans]=0
            