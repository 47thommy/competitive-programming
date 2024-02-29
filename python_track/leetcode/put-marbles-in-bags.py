class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        arr=[]
        for i in range(len(weights)-1):
            arr.append(weights[i]+weights[i+1])
        arr.sort()
        print(arr)
        if(k-1==0):
            return 0
        maxi=sum(arr[-k+1:])
        mini=sum(arr[:k-1])
        return maxi-mini