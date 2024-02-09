class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum=[]
        suffix_sum=[]
        end=len(nums)-1
        running_p=0
        running_s=0
        for i in range(len(nums)):
            prefix_sum.append(running_p)
            suffix_sum.append(running_s)
            running_p+=nums[i]
            running_s+=nums[end]
            end-=1
        ans=[] 
        end=len(suffix_sum)-1
        for j in range(len(nums)):
            value=suffix_sum[end]-prefix_sum[j]+j*nums[j]-(len(nums)-(j+1))*nums[j]
            end-=1
            ans.append(value)
        return ans
            