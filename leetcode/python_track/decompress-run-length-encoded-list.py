class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        l=0
        while l<len(nums)-1:
            fre=nums[l]
            val=nums[l+1]
            for _ in range(fre):
                res.append(val)
            l+=2
        return res
            
        