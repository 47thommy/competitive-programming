from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        counter_list=Counter(nums)
        res=[]
        
        for key in counter_list.keys():
          
            if counter_list[key] > n //3:
                res.append(key)
        return res
        
                
            
        