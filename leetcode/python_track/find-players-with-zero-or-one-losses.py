from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner=[]
        one_time_losers=[]
        val=[]
        res=[]
        check=defaultdict(list)
        for i in range(len(matches)):
            check[matches[i][1]].append(matches[i][0])
        for key,value in check.items():
            if len(value)==1:
                one_time_losers.append(key)
        
        for v in check.values():
            val+=v
        sval=set(val)
        for s in sval:
            if s not in check:
                winner.append(s)
        winner.sort()
        one_time_losers.sort()
        res.append(winner)
        res.append(one_time_losers)
        return res 
            
        
            
            
            