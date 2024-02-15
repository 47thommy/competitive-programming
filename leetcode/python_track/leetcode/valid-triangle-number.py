class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        right=len(nums)-1
        print(nums)
        for i in range(len(nums)-1,1,-1):
            left=0
            right=i-1
            while left < right:
                if nums[left]+nums[right]<=nums[i]:
                    left+=1
                else:
                    ans+=right-left
                    right-=1
        return ans

