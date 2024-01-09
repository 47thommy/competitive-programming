class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        sum=0
        ans=0
        for end in range(len(nums)):            
            if nums[end]==0:
                sum+=1
            while sum >1:
                if nums[left]==0:
                    sum-=1
                left+=1
            ans=max(ans,end-left+1)
        return ans-1