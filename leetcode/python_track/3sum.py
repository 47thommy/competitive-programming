class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target1=nums[i]
            l,r=i+1,len(nums)-1
            while l<r:
                threesum=target1+nums[r]+nums[l]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return ans
                
            
            
            