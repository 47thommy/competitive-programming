class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        left=0

        total=0
        currentTotal=0
        check={}
        for end in range(len(nums)):
            check[nums[end]]=check.get(nums[end],0)+1
            currentTotal+=nums[end]
            while len(check.keys())<end-left+1:
                check[nums[left]]-=1
                currentTotal-=nums[left]
                if check[nums[left]]==0:
                    del check[nums[left]]
                left+=1
                
            total=max(total,currentTotal)
        
        return total
 