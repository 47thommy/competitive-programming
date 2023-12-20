class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=[]
        for i in range(len(digits)):
            s.append(str(digits[i]))
        largest=int("".join(s))+1   
        return map(int,list(str(largest)))
        
            