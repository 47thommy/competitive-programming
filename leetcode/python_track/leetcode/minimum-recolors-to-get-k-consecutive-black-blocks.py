from collections import Counter
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        block=[]
        for i in range(len(blocks)):
            block.append(blocks[i])
        left=0
        whiteCount=Counter(block[left:k])["W"]
        currentCount=whiteCount
        for right in range(k,len(block)):
            if block[right]=="W":
                currentCount +=1
            if block[left]=="W":
                currentCount-=1
            left+=1
            whiteCount=min(whiteCount,currentCount)
        return whiteCount
                