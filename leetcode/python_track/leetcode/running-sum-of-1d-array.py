class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rmap={}
        for i in range (len(nums)):
            rmap[i]=rmap.get(i-1,0)+nums[i]
        return rmap.values()