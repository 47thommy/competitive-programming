from collections import Counter
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        check=set(fronts + backs)
        for i in range(len(backs)):
            if backs[i]==fronts [i] and backs[i] in check:
                check.remove(backs[i])
        if len(check)==0:
            return 0
        else:
            return check.pop()