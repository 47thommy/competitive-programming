class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        sum=0
        ans=float('inf')
        for end in range(len(nums)):     
            sum+=nums[end]
            while sum >=target:
                sum-=nums[left]
                ans=min(ans,end-left+1)
                left+=1
        if ans == float('inf'):
            return 0
        else:
            return ans