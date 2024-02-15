class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        number=target
        arr=[]
        while maxDoubles>0 and number>2:
            number=number//2
            arr.append(number)
            maxDoubles-=1
        ptr=1
        ans=0
        if len(arr)==0:
            return target - 1
        for i in range(len(arr)-1,-1,-1):
            ans+=arr[i]-ptr+1
            
            ptr=2*arr[i]     
        ans+=target-arr[0]*2
        return ans



