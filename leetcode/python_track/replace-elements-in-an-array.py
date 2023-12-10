class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_dictionary={}
        ans=[]
        for i,n in enumerate(nums):
            nums_dictionary[n]=i
        for operation in operations:
            value=nums_dictionary[operation[0]]
            nums_dictionary.pop(operation[0])
            nums_dictionary[operation[1]]=value
        sorted_dict = sorted(nums_dictionary.items(), key=lambda x:x[1])
        for i in range(len(sorted_dict)):
            ans.append(sorted_dict[i][0])
        return ans
            
            
            
        
            