class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        sum=0
        ans=0
        for end in range(len(nums)):            
            if nums[end]==0:
                sum+=1
            while sum >k:
                if nums[left]==0:
                    sum-=1
                left+=1
            ans=max(ans,end-left+1)
        return ans