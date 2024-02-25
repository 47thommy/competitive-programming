from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQueue=deque()
        dQueue=deque()
        for i in range(len(senate)):
            if senate[i]=="R":
                rQueue.append(i)
            else:
                dQueue.append(i)
        pt=0
        while rQueue and dQueue:
            if rQueue[pt]<dQueue[pt]:
                dQueue.popleft()
                rQueue.append(rQueue.popleft()+len(senate))
            else:
                rQueue.popleft()
                dQueue.append(dQueue.popleft()+len(senate))
        return "Radiant" if rQueue else "Dire"