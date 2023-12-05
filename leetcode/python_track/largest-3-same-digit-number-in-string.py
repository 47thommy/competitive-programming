class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                temp=num[i]+num[i+1]+num[i+2]
                print(ans)
                if ans=="":
                    ans=0
                ans=str(max(int(temp),int(ans)))
              
        if ans ==0:
            ans = ""
        elif ans == "0":
            ans="000"
        return ans
                