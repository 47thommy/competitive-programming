class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        kmap={}
        kmap[0]=1
        res=0
        left=0
        currsum=0
        for num in nums:
            currsum+=num
            diff=currsum-k
            res+=kmap.get(diff,0)
            kmap[currsum]=kmap.get(currsum,0)+1
        print(kmap)
        return res
            
            
            
        
        
            
        