from collections import defaultdict 
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        check=defaultdict(list) 
        for i in range(len(list1)):
            if list1[i] in list2:
                ind = list2.index(list1[i])
                t = ind + i
                check[t].append(list1[i]) 
        a=min(check.keys())
        return check[a]
            
            
                
                