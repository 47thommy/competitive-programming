class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target=len(set(nums))
        count={}
        size=0
        ans=0
        start=0
        for end in range(len(nums)):            
            if nums[end] not in count:
                size+=1
            count[nums[end]]=count.get(nums[end],0)+1
            while size == target :
                ans+=len(nums)-end
                count[nums[start]]-=1
                if count[nums[start]]==0:
                    del count[nums[start]]
                    size-=1
                start+=1
        return ans