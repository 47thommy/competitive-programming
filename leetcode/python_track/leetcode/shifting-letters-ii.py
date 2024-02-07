class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr=[0]*len(s)
        for shift in shifts:
            if shift[-1]==0:
                arr[shift[0]]-=1
                if shift[1]<len(s)-1:
                    arr[shift[1]+1]+=1
            elif shift[-1]==1:
                arr[shift[0]]+=1
                if shift[1]<len(s)-1:
                    arr[shift[1]+1]-=1
        prefix_sum=[]
        running_sum=0
        for i in range(len(arr)):
            running_sum+=arr[i]
            prefix_sum.append(running_sum)
        ans=[]
        
        for i in range(len(s)):
            value=(ord(s[i])+prefix_sum[i]-ord("a"))%26
            ans.append(chr(value+ord("a")))
        return "".join(ans)
                