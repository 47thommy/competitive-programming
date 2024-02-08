class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product=[]
        running_prefix_product=1
        suffix_product=[]
        running_suffix_product=1
        for i in range(len(nums)):
            prefix_product.append(running_prefix_product)
            suffix_product.append(running_suffix_product)   
            running_prefix_product*=nums[i]
            running_suffix_product*=nums[len(nums)-i-1]
        ans=[]
        right=len(nums)-1
        for left in range(len(nums)):
            value=prefix_product[left]*suffix_product[right]
            right-=1
            ans.append(value)
        return ans
            
        