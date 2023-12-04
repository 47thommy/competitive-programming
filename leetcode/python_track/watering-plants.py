class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=0
        right=0
        left=0
        c=capacity
        while right<len(plants):
            if(plants[right]<=c):
                c=c-plants[right]
                right+=1
                steps+=1
            else:
                steps+=(right)*2
                c=capacity
        return steps
                
                
                
                
                
                
            