class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        check={}
        start=0
        ans=0
        for end in range(len(nums)):
            check[nums[end]]=check.get(nums[end],0)+1
            while check [nums[end]]>k:
                check[nums[start]]-=1
                if check[nums[start]]==0:
                    del check[nums[start]]
                start+=1
            ans=max(ans,end-start+1)
        return ans