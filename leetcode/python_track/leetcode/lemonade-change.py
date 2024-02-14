class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        flag = True
        visited={}
        for bill in bills:
            if bill == 10:
                if 5 not in visited:
                    flag=False
                else:
                    visited[5]-=1
                    if visited[5]==0:
                        del visited[5]
            if bill == 20:
                if 10 in visited and 5 in visited:
                    visited[10]-=1
                    visited[5]-=1
                    if visited[10]==0:
                        del visited[10]
                    if visited[5]==0:
                        del visited[5]
                elif 5 in visited and visited[5]>=3:
                    visited[5]-=3
                else:
                    flag=False
            visited[bill]=visited.get(bill,0)+1
        return flag


