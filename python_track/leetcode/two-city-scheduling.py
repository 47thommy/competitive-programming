class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff=[]
        for i in range(len(costs)):
            diff.append([costs[i][0]-costs[i][1],i])
        diff.sort()
        ans=0
        for i in range((len(costs)//2)):
            ans+=costs[diff[i][1]][0]
       
        for i in range(len(costs)-1,(len(costs)//2)-1,-1):
            ans+=costs[diff[i][1]][1]
        return ans