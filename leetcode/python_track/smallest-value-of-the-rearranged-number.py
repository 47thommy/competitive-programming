class Solution:
    def smallestNumber(self, num: int) -> int:
        nums=list(str(num))
        nnums=list(str(num))[1:]
        first=nums[0]
        for i in range(len(nums)):
            if nums[i]!="0":
                first=min(nums[i],first)
        nums.remove(first)
        nums.sort()
        ans=first+"".join(nums)
        if num<0:
            nnums.sort(reverse=True)
            return -(int("".join(nnums)))  
        else:
            
            return int(ans)
        
                
            