import math
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>nums[i+1]:
                spaces=math.ceil(nums[i]/nums[i+1])
                ans+=spaces-1
                nums[i]=nums[i]//spaces
        return ans


