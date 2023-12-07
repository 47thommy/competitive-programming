class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        cs=set()
        for i in range(0, len(nums)):
            cs.add(i)
    
        cs.add(i+1)
        res=cs.difference(set(nums))
        return res.pop()
            