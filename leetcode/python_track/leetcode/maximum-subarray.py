class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum = nums[0]  
        sum = nums[0] 
        for i in range(1, len(nums)):
            sum = max(nums[i], sum + nums[i])
            msum = max(msum, sum)

        return msum
