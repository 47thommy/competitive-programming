from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return 0
        operations=0
        nums.sort()
        count=Counter(nums)
        keys=list(count.keys())
        print(count)
        j=len(keys)-1
        for i in range(len(keys)-1,0,-1):
            operations+=count[keys[j]]
            count[keys[j-1]]+=count[keys[j]]
            del count[keys[j]]
            j-=1
            
        return operations
        
                
                