class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set=set(nums)
        nums2=list(nums_set)
        nums2.sort()
        
        if len(nums2)<3:
            return nums2[-1]
        return nums2[-3]