class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        arr=[]
        ans=0
        for i in range(len(s)):
            if s[i] =="(":
                arr.append(s[i])
            else:
                if len(arr)>0:
                    arr.pop()
                else:
                    ans+=1
        ans+=len(arr)
        return ans
