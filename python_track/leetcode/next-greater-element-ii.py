class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        
        for idx, val in enumerate(nums): 
            while stack and val > nums[stack[-1]]:
                result[stack.pop()] = val   
            stack.append(idx)
            
        for idx, val in enumerate(nums):  
            while stack and val > nums[stack[-1]]:
                result[stack.pop()] = val
        return result