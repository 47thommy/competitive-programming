from collections import Counter
import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        ans=0
        for key in count:
            if key==0:
                ans+=count[key]
            else:
                ans+=math.ceil(count[key]/(key+1))*(key+1)
        return ans