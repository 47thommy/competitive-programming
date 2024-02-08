class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr=[0]*1000
        for trip in trips:
            arr[trip[1]]+=trip[0]
            if trip[2]<1000:
                arr[trip[2]]-=trip[0]
        prefix_sum=[]
        running_sum=0
        for i in range(len(arr)):
            running_sum+=arr[i]
            prefix_sum.append(running_sum)
        value=max(prefix_sum)
        return value<=capacity