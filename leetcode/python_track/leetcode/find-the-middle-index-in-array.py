class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum=[0]
        running_sum=0
        for i in range(len(nums)):
            running_sum+=nums[i]
            prefix_sum.append(running_sum)
        for j in range (1,len(prefix_sum)):
            if prefix_sum[j-1]==prefix_sum[-1]-prefix_sum[j]:
                return j-1
        return -1
            
            