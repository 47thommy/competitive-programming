class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr=[0]*len(nums)
        for request in requests:
            arr[request[0]]+=1
            if request[1]+1<len(nums):
                arr[request[1]+1]-=1
        prefix_sum=[]
        running_sum=0
        for i in range(len(arr)):
            running_sum+=arr[i]
            prefix_sum.append(running_sum)
        prefix_sum.sort()    
        nums.sort()
        ans=0
        for j in range(len(nums)):
            ans+=prefix_sum[j]*nums[j]
        return ans % (10**9+7)