class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr)):
            idx=arr.index(max(arr))
            l,r=0,idx
            ans.append(idx+1)
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            l,r=0,len(arr)-1
            ans.append(r+1)
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1   
            arr.pop()
        return ans
                