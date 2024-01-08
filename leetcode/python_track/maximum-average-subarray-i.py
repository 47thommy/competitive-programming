class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float: 
        l = 0
        current = sum(nums[l:k])
        mTotal = current
        for idx in range(k,len(nums)):
            current = current-nums[l]+nums[idx]
            mTotal=max(mTotal,current)
            l += 1         
        return mTotal/k

            
        



            

