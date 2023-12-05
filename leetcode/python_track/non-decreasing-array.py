class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count=0
        
        
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
                if i!=0 and nums[i-1]>nums[i+1]:
                    count+=1 
        print(count)
        c=0   
        if count>1:
            t=0
            while t<len(nums)-1:
                if nums[t]<=nums[t+1]:
                    c+=1
                    t+=1
                elif t<len(nums)-2 and nums[t]<=nums[t+2] : 
                    c+=1
                    t+=2
                else:
                    t+=2
             
            print(c)
            if c == len(nums)-2:
                return True
            else:
                return False    
        else:
            return True
                
                