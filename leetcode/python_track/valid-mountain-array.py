class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maximum=max(arr)
        i=arr.index(maximum)
        print(i)
        if (i==0 or len(arr)<3 or i==len(arr)-1):
            return False
        l=0
        while l<i:
            if arr[l]>=arr[l+1]:
                print("hjkl")
                return False
            l+=1
        r=i
        while r<len(arr)-1:
            if arr[r] <= arr[r+1]:
                return False
            r+=1
        return True
            
            
            
            