class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr=[0]*n
        for book in bookings:
            arr[book[0]-1]+=book[-1]
            if book[1]<n:
                arr[book[1]]-=book[-1]
        prefix_sum=[]
        running_sum=0
        for i in range(len(arr)):
            running_sum+=arr[i]
            prefix_sum.append(running_sum)
        return prefix_sum
        