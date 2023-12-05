class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dis=[]
        for i in range(len(ghosts)):
            # temp=(ghosts[i][0]-target[0])**2+(ghosts[i][1]-target[1])**2
            temp = abs(ghosts[i][0]-target[0]) + abs(ghosts[i][1]-target[1])
            dis.append(temp)
        print(sum(target), min(dis))
        return min(dis)> (abs(target[0])+abs(target[1]))
            