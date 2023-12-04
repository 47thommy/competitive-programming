class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=float('-inf')
        count=0
        for num in nums:
            if num==1:
                count+=1
            else:
                count=0
            m=max(m,count)
        return m
                
        