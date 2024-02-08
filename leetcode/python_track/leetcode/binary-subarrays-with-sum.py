class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum=[]
        running_sum=0
        for i in range(len(nums)):
            running_sum+=nums[i]
            prefix_sum.append(running_sum)
        hashmap={}
        count=0
        print(prefix_sum)
        for j in range(len(prefix_sum)):
            if prefix_sum[j]-goal in hashmap:
                count+=hashmap[prefix_sum[j]-goal]
            if prefix_sum[j]-goal ==0:
                count+=1
            hashmap[prefix_sum[j]]=hashmap.get(prefix_sum[j],0)+1
        return count
            