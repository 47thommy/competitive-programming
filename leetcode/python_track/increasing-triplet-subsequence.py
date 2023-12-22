class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        left, middle = float("inf"), float("inf")
        
        for right in nums:
            
            if middle < right:
                return True
            if right <= left:
                left= right    
            else:
                middle = right 
                
        return  False