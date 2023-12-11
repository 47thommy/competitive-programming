class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        maximum=0
        while len(nums_set)>0:
            low=high=nums_set.pop()
            while low-1 in nums_set:
                nums_set.remove(low-1)
                low-=1
            while high+1 in nums_set:
                nums_set.remove(high+1)
                high+=1
            maximum=max(high-low+1, maximum)    
        return maximum
                
                
        
            